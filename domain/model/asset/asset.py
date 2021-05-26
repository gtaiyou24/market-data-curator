from __future__ import annotations

from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class Asset:
    """「資産」

    ファイナンスでは、株式、債券、短期金融、資産、不動産など資産クラスを指すときは、「資産(Asset)」
    資産クラスの中の個別銘柄を指すときは「証券(Security)」という用語を使うことが多いが、
    本パッケージでは「資産」という用語を用いることにする。
    """
    name: str

    def __init__(self, name: str):
        assert isinstance(name, str), "資産名には文字列を指定してください。"
        assert name, "資産名は必須です。"
        super().__setattr__("name", name)
