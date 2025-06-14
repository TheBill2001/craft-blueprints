import info
from Package.BlueprintRepositoryPackageBase import BlueprintRepositoryPackageBase


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["master"] = (
            f"[git]https://github.com/TheBill2001/craft-blueprints-thebill2001|master|"
        )
        self.defaultTarget = "master"

    def setDependencies(self):
        self.buildDependencies["craft/craft-core"] = None


class Package(BlueprintRepositoryPackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
