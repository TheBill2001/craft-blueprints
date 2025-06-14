import os
import info
import utils
from Package.CMakePackageBase import CMakePackageBase
from CraftCore import CraftCore


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "Mass Effect: Andronmeda Save Editor"
        self.webpage = "https://github.com/TheBill2001/mea-save-editor"
        self.svnTargets["master"] = "https://github.com/TheBill2001/mea-save-editor.git|main"
        self.defaultTarget = "master"

        # We will move these manually, Craft seem to be messing this up
        self.options.package.movePluginsToBin = False
        self.options.package.moveTranslationsToBin = False

    def registerOptions(self):
        self.parent.package.categoryInfo.platforms = CraftCore.compiler.Platforms.Windows | CraftCore.compiler.Platforms.Linux

    def setDependencies(self):
        self.buildDependencies["dev-utils/cmake"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None

        self.runtimeDependencies["libs/qt6/qtbase"] = None


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        CMakePackageBase.buildTests = False

    @property
    def applicationExecutable(self):
        return "mea-save-editor"

    def createPackage(self):
        if not CraftCore.compiler.isLinux:
            self.ignoredPackages += [
                "libs/dbus",
                "libs/qt6/qtwayland",
            ]

        self.defines["shortcuts"] = [
            {"name": self.subinfo.displayName, "target": f"bin/{self.applicationExecutable}.exe"}
        ]

        self.addExecutableFilter(fr"bin/(?!({self.applicationExecutable})).*")

        self.blacklist_file.append(os.path.join(self.blueprintDir(), "blacklist.txt"))

        return super().createPackage()

    def preArchive(self):
        # We will move these manually, Craft seem to be messing this up
        utils.mergeTree(self.archiveDir() / "bin", self.archiveDir())
        return super().preArchive()
