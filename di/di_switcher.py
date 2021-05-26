import os
from typing import Dict, Set, Any

from di import Profile


ENV_NAME = "PROFILE_ACTIVES"


class DISwitcher:
    PROFILE_ACTIVES: Set[str] = set(os.getenv(ENV_NAME).split(","))

    @classmethod
    def get(cls, interfaces: Dict[Profile, Any]) -> Any:
        for profile, interface in interfaces.items():
            if profile.match(cls.PROFILE_ACTIVES):
                return interface

        return None
        # raise ValueError("該当のインターフェースが見つかりませんでした(PROFILE_ACTIVES={})".format(cls.PROFILE_ACTIVES))
