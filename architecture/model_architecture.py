
import torch
import torch.nn as nn

class MLPMapper(nn.Module):
    def __init__(self, clip_dim=512, gpt2_dim=768, prefix_len=10):
        super().__init__()
        self.prefix_len = prefix_len
        self.gpt2_dim = gpt2_dim
        self.mlp = nn.Sequential(
            nn.Linear(clip_dim, 512), nn.GELU(), nn.Dropout(0.1),
            nn.Linear(512, 512), nn.GELU(),
            nn.Linear(512, prefix_len * gpt2_dim)
        )

    def forward(self, x):
        return self.mlp(x).view(-1, self.prefix_len, self.gpt2_dim)


class TransformerMapper(nn.Module):
    def __init__(self, clip_dim=512, gpt2_dim=768, prefix_len=10, clip_project_len=10,
                 num_layers=8, num_heads=8):
        super().__init__()
        self.prefix_len = prefix_len
        self.clip_project_len = clip_project_len
        self.gpt2_dim = gpt2_dim
        self.linear = nn.Linear(clip_dim, clip_project_len * gpt2_dim)
        self.prefix_const = nn.Parameter(torch.randn(prefix_len, gpt2_dim) * 0.02)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=gpt2_dim, nhead=num_heads, dim_feedforward=gpt2_dim * 2,
            dropout=0.1, activation="gelu", batch_first=True, norm_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

    def forward(self, x):
        b = x.shape[0]
        visual_tokens = self.linear(x).view(b, self.clip_project_len, self.gpt2_dim)
        prefix_tokens = self.prefix_const.unsqueeze(0).expand(b, -1, -1)
        tokens = torch.cat([visual_tokens, prefix_tokens], dim=1)
        out = self.transformer(tokens)
        return out[:, self.clip_project_len:]


def load_clipcap_model(checkpoint_path, device="cpu"):
    # Load model ClipCap (MLP atau Transformer mapping network) untuk dipakai
    # di VSCode / deployment di luar Colab.
    #
    # Usage:
    #     from model_architecture import load_clipcap_model
    #     mapping_net, gpt2, tokenizer, clip_model, preprocess, config = load_clipcap_model(
    #         "clipcap_pretrained_coco.pth", device="cuda"
    #     )
    import clip
    from transformers import GPT2LMHeadModel, GPT2Tokenizer

    ckpt = torch.load(checkpoint_path, map_location=device)
    config = ckpt["config"]

    if config["mapping_type"] == "transformer":
        mapping_net = TransformerMapper(
            clip_dim=config["clip_dim"], gpt2_dim=config["gpt2_dim"],
            prefix_len=config["prefix_len"], clip_project_len=config["clip_project_len"],
            num_layers=config["transformer_layers"], num_heads=config["transformer_heads"],
        ).to(device)
    else:
        mapping_net = MLPMapper(
            clip_dim=config["clip_dim"], gpt2_dim=config["gpt2_dim"], prefix_len=config["prefix_len"]
        ).to(device)
    mapping_net.load_state_dict(ckpt["mapping_net_state_dict"])

    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)
    gpt2_model.load_state_dict(ckpt["gpt2_state_dict"])

    clip_model, preprocess = clip.load(config["clip_backbone"], device=device)

    return mapping_net, gpt2_model, tokenizer, clip_model, preprocess, config
