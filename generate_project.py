import os

os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# ─── 1. project.pbxproj ───────────────────────────────────────────────────────
pbxproj_content = """// !$*UTF8*$!
{
\tarchiveVersion = 1;
\tclasses = {
\t};
\tobjectVersion = 56;
\tobjects = {

/* Begin PBXBuildFile section */
\t\t010101012C12345600000001 /* UTanApp.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000002 /* UTanApp.swift */; };
\t\t010101012C12345600000003 /* Scraper.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000004 /* Scraper.swift */; };
\t\t010101012C12345600000005 /* CustomPlayer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000006 /* CustomPlayer.swift */; };
\t\t010101012C12345600000007 /* SubtitleParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000008 /* SubtitleParser.swift */; };
\t\t010101012C12345600000009 /* Views.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000000A /* Views.swift */; };
\t\t010101012C1234560000001A /* logo.png in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000001B /* logo.png */; };
\t\t010101012C1234560000001C /* Netflix.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000001D /* Netflix.jpg */; };
\t\t010101012C1234560000001E /* Anime.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000001F /* Anime.jpg */; };
\t\t010101012C12345600000020 /* Kids.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000021 /* Kids.jpg */; };
\t\t010101012C12345600000022 /* Hbo.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000023 /* Hbo.jpg */; };
\t\t010101012C12345600000024 /* Disney.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000025 /* Disney.jpg */; };
\t\t010101012C12345600000026 /* Marvel.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000027 /* Marvel.jpg */; };
\t\t010101012C12345600000028 /* Cairo.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000029 /* Cairo.ttf */; };
\t\t010101012C1234560000002A /* Cairo-Bold-1.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000002B /* Cairo-Bold-1.ttf */; };
\t\t010101012C1234560000002C /* Rubik.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000002D /* Rubik.ttf */; };
\t\t010101012C1234560000002E /* Rubik-Bold.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000002F /* Rubik-Bold.ttf */; };
\t\t010101012C12345600000030 /* Ibm.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000031 /* Ibm.ttf */; };
\t\t010101012C12345600000032 /* IBMPlexArabic-Bold.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000033 /* IBMPlexArabic-Bold.ttf */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
\t\t010101012C12345600000002 /* UTanApp.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = UTanApp.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000004 /* Scraper.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Scraper.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000006 /* CustomPlayer.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = CustomPlayer.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000008 /* SubtitleParser.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = SubtitleParser.swift; sourceTree = "<group>"; };
\t\t010101012C1234560000000A /* Views.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Views.swift; sourceTree = "<group>"; };
\t\t010101012C1234560000000B /* Info.plist */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
\t\t010101012C1234560000000C /* UTan.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = UTan.app; sourceTree = BUILT_PRODUCTS_DIR; };
\t\t010101012C1234560000001B /* logo.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; path = logo.png; sourceTree = "<group>"; };
\t\t010101012C1234560000001D /* Netflix.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Netflix.jpg; sourceTree = "<group>"; };
\t\t010101012C1234560000001F /* Anime.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Anime.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000021 /* Kids.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Kids.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000023 /* Hbo.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Hbo.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000025 /* Disney.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Disney.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000027 /* Marvel.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Marvel.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000029 /* Cairo.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = Cairo.ttf; sourceTree = "<group>"; };
\t\t010101012C1234560000002B /* Cairo-Bold-1.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "Cairo-Bold-1.ttf"; sourceTree = "<group>"; };
\t\t010101012C1234560000002D /* Rubik.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = Rubik.ttf; sourceTree = "<group>"; };
\t\t010101012C1234560000002F /* Rubik-Bold.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "Rubik-Bold.ttf"; sourceTree = "<group>"; };
\t\t010101012C12345600000031 /* Ibm.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = Ibm.ttf; sourceTree = "<group>"; };
\t\t010101012C12345600000033 /* IBMPlexArabic-Bold.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "IBMPlexArabic-Bold.ttf"; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
\t\t010101012C1234560000000D /* Frameworks */ = {
\t\t\tisa = PBXFrameworksBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
\t\t010101012C1234560000000E /* MainGroup */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t010101012C1234560000000F /* UTan */,
\t\t\t\t010101012C1234560000000C /* UTan.app */,
\t\t\t);
\t\t\tsourceTree = "<group>";
\t\t};
\t\t010101012C1234560000000F /* UTan */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t010101012C12345600000002 /* UTanApp.swift */,
\t\t\t\t010101012C12345600000004 /* Scraper.swift */,
\t\t\t\t010101012C12345600000006 /* CustomPlayer.swift */,
\t\t\t\t010101012C12345600000008 /* SubtitleParser.swift */,
\t\t\t\t010101012C1234560000000A /* Views.swift */,
\t\t\t\t010101012C1234560000000B /* Info.plist */,
\t\t\t\t010101012C1234560000001B /* logo.png */,
\t\t\t\t010101012C1234560000001D /* Netflix.jpg */,
\t\t\t\t010101012C1234560000001F /* Anime.jpg */,
\t\t\t\t010101012C12345600000021 /* Kids.jpg */,
\t\t\t\t010101012C12345600000023 /* Hbo.jpg */,
\t\t\t\t010101012C12345600000025 /* Disney.jpg */,
\t\t\t\t010101012C12345600000027 /* Marvel.jpg */,
\t\t\t\t010101012C12345600000029 /* Cairo.ttf */,
\t\t\t\t010101012C1234560000002B /* Cairo-Bold-1.ttf */,
\t\t\t\t010101012C1234560000002D /* Rubik.ttf */,
\t\t\t\t010101012C1234560000002F /* Rubik-Bold.ttf */,
\t\t\t\t010101012C12345600000031 /* Ibm.ttf */,
\t\t\t\t010101012C12345600000033 /* IBMPlexArabic-Bold.ttf */,
\t\t\t);
\t\t\tpath = UTan;
\t\t\tsourceTree = "<group>";
\t\t};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
\t\t010101012C12345600000010 /* UTan */ = {
\t\t\tisa = PBXNativeTarget;
\t\t\tbuildConfigurationList = 010101012C12345600000011;
\t\t\tbuildPhases = (
\t\t\t\t010101012C12345600000012 /* Sources */,
\t\t\t\t010101012C1234560000000D /* Frameworks */,
\t\t\t\t010101012C12345600000034 /* Resources */,
\t\t\t);
\t\t\tbuildRules = (
\t\t\t);
\t\t\tdependencies = (
\t\t\t);
\t\t\tname = UTan;
\t\t\tproductName = UTan;
\t\t\tproductReference = 010101012C1234560000000C /* UTan.app */;
\t\t\tproductType = "com.apple.product-type.application";
\t\t};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
\t\t010101012C12345600000013 /* Project object */ = {
\t\t\tisa = PBXProject;
\t\t\tattributes = {
\t\t\t\tLastSwiftUpdateCheck = 1500;
\t\t\t\tLastUpgradeCheck = 1500;
\t\t\t\tTargetAttributes = {
\t\t\t\t\t010101012C12345600000010 = {
\t\t\t\t\t\tCreatedOnToolsVersion = 15.0;
\t\t\t\t\t\tDevelopmentTeam = "";
\t\t\t\t\t};
\t\t\t\t};
\t\t\t};
\t\t\tbuildConfigurationList = 010101012C12345600000014;
\t\t\tcompatibilityVersion = "Xcode 14.0";
\t\t\tdevelopmentRegion = en;
\t\t\thasScannedForEncodings = 0;
\t\t\tknownRegions = (
\t\t\t\ten,
\t\t\t\tBase,
\t\t\t\tar,
\t\t\t);
\t\t\tmainGroup = 010101012C1234560000000E;
\t\t\tproductRefGroup = 010101012C1234560000000E;
\t\t\tprojectDirPath = "";
\t\t\tprojectRoot = "";
\t\t\ttargets = (
\t\t\t\t010101012C12345600000010 /* UTan */,
\t\t\t);
\t\t};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
\t\t010101012C12345600000034 /* Resources */ = {
\t\t\tisa = PBXResourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t\t010101012C1234560000001A /* logo.png in Resources */,
\t\t\t\t010101012C1234560000001C /* Netflix.jpg in Resources */,
\t\t\t\t010101012C1234560000001E /* Anime.jpg in Resources */,
\t\t\t\t010101012C12345600000020 /* Kids.jpg in Resources */,
\t\t\t\t010101012C12345600000022 /* Hbo.jpg in Resources */,
\t\t\t\t010101012C12345600000024 /* Disney.jpg in Resources */,
\t\t\t\t010101012C12345600000026 /* Marvel.jpg in Resources */,
\t\t\t\t010101012C12345600000028 /* Cairo.ttf in Resources */,
\t\t\t\t010101012C1234560000002A /* Cairo-Bold-1.ttf in Resources */,
\t\t\t\t010101012C1234560000002C /* Rubik.ttf in Resources */,
\t\t\t\t010101012C1234560000002E /* Rubik-Bold.ttf in Resources */,
\t\t\t\t010101012C12345600000030 /* Ibm.ttf in Resources */,
\t\t\t\t010101012C12345600000032 /* IBMPlexArabic-Bold.ttf in Resources */,
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
\t\t010101012C12345600000012 /* Sources */ = {
\t\t\tisa = PBXSourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t\t010101012C12345600000001 /* UTanApp.swift in Sources */,
\t\t\t\t010101012C12345600000003 /* Scraper.swift in Sources */,
\t\t\t\t010101012C12345600000005 /* CustomPlayer.swift in Sources */,
\t\t\t\t010101012C12345600000007 /* SubtitleParser.swift in Sources */,
\t\t\t\t010101012C12345600000009 /* Views.swift in Sources */,
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
\t\t010101012C12345600000015 /* Debug */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = dwarf;
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tENABLE_TESTABILITY = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu11;
\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tGCC_OPTIMIZATION_LEVEL = 0;
\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = ( "DEBUG=1", "$(inherited)", );
\t\t\t\tMTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tONLY_ACTIVE_ARCH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-Onone";
\t\t\t};
\t\t\tname = Debug;
\t\t};
\t\t010101012C12345600000016 /* Release */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
\t\t\t\tENABLE_NS_ASSERTIONS = NO;
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu11;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_COMPILATION_MODE = wholemodule;
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-O";
\t\t\t\tVALIDATE_PRODUCT = YES;
\t\t\t};
\t\t\tname = Release;
\t\t};
\t\t010101012C12345600000017 /* Debug Target */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCODE_SIGNING_ALLOWED = NO;
\t\t\t\tCODE_SIGNING_REQUIRED = NO;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tINFOPLIST_FILE = UTan/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 16.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = ( "$(inherited)", "@executable_path/Frameworks", );
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t};
\t\t\tname = Debug;
\t\t};
\t\t010101012C12345600000018 /* Release Target */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCODE_SIGNING_ALLOWED = NO;
\t\t\t\tCODE_SIGNING_REQUIRED = NO;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tINFOPLIST_FILE = UTan/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 16.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = ( "$(inherited)", "@executable_path/Frameworks", );
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t};
\t\t\tname = Release;
\t\t};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
\t\t010101012C12345600000011 = {
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t010101012C12345600000017 /* Debug */,
\t\t\t\t010101012C12345600000018 /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t};
\t\t010101012C12345600000014 = {
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t010101012C12345600000015 /* Debug */,
\t\t\t\t010101012C12345600000016 /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t};
/* End XCConfigurationList section */
\t};
\trootObject = 010101012C12345600000013 /* Project object */;
}
"""
with open("UTan/UTan.xcodeproj/project.pbxproj", "w", encoding="utf-8") as f:
    f.write(pbxproj_content)

# ─── 2. Info.plist  (يسجل كل الخطوط صراحةً) ──────────────────────────────────
info_plist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key><string>en</string>
    <key>CFBundleExecutable</key><string>$(EXECUTABLE_NAME)</string>
    <key>CFBundleIdentifier</key><string>com.mustaqil.utan</string>
    <key>CFBundleInfoDictionaryVersion</key><string>6.0</string>
    <key>CFBundleName</key><string>UTan</string>
    <key>CFBundlePackageType</key><string>APPL</string>
    <key>CFBundleShortVersionString</key><string>5.0</string>
    <key>CFBundleVersion</key><string>5</string>
    <key>LSRequiresIPhoneOS</key><true/>
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key><true/>
    </dict>
    <key>UIBackgroundModes</key>
    <array><string>fetch</string><string>processing</string></array>
    <key>UILaunchScreen</key><dict/>
    <key>UISupportedInterfaceOrientations</key>
    <array>
        <string>UIInterfaceOrientationPortrait</string>
        <string>UIInterfaceOrientationLandscapeLeft</string>
        <string>UIInterfaceOrientationLandscapeRight</string>
    </array>
    <key>UIUserInterfaceStyle</key><string>Dark</string>
    <key>UIAppFonts</key>
    <array>
        <string>Cairo.ttf</string>
        <string>Cairo-Bold-1.ttf</string>
        <string>Rubik.ttf</string>
        <string>Rubik-Bold.ttf</string>
        <string>Ibm.ttf</string>
        <string>IBMPlexArabic-Bold.ttf</string>
    </array>
</dict>
</plist>
"""
with open("UTan/UTan/Info.plist", "w", encoding="utf-8") as f:
    f.write(info_plist)

# ─── 3. UTanApp.swift (مع إضافة import UIKit) ─────────────────────────────────
app_swift = """import SwiftUI
import UIKit

@main
struct UTanApp: App {
    init() {
        // طباعة جميع الخطوط المسجلة في iOS للتحقق
        debugPrintFonts()
    }
    var body: some Scene {
        WindowGroup { MainTabView() }
    }
    private func debugPrintFonts() {
        #if DEBUG
        print("=== Registered Font Families ===")
        for family in UIFont.familyNames.sorted() {
            let names = UIFont.fontNames(forFamilyName: family)
            if names.contains(where: { $0.lowercased().contains("cairo") || $0.lowercased().contains("rubik") || $0.lowercased().contains("ibm") }) {
                print("Family: \\(family)")
                for name in names { print("  → \\(name)") }
            }
        }
        print("================================")
        #endif
    }
}
"""
with open("UTan/UTan/UTanApp.swift", "w", encoding="utf-8") as f:
    f.write(app_swift)

print("✅ الملفات الأساسية كُتبت (pbxproj / Info.plist / UTanApp)")

# ─── 4. Scraper.swift (مع إضافة import UIKit) ─────────────────────────────────
scraper_swift = r"""import Foundation
import SwiftUI
import UIKit      // لـ UISaveVideoAtPathToSavedPhotosAlbum و UIFont

// ─────────────────────────────────────────────
// MARK: – Global Colors
// ─────────────────────────────────────────────
let APP_BG     = Color(red: 0.05, green: 0.02, blue: 0.09)
let UT_RED     = Color(red: 0.89, green: 0.04, blue: 0.08)
let UT_WHITE   = Color.white
let UT_SURFACE = Color.white.opacity(0.12)

// ─────────────────────────────────────────────
// MARK: – AppSettings
// ─────────────────────────────────────────────
class AppSettings: ObservableObject {
    static let shared = AppSettings()
    @AppStorage("sub_fontSize")   var subtitleFontSize: Double  = 22.0
    @AppStorage("sub_colorHex")   var subtitleColorHex: String  = "#FFFFFF"
    @AppStorage("sub_bgOpacity")  var subtitleBgOpacity: Double = 0.6
    @AppStorage("sub_bottomPad")  var subtitleBottomPad: Double = 60.0
    @AppStorage("sub_enabled")    var subtitlesEnabled: Bool    = true
    @AppStorage("sub_fontName")   var subtitleFontName: String  = "Cairo-Regular"

    var subtitleColor: Color { Color(hex: subtitleColorHex) }

    func clearCache() {
        URLCache.shared.removeAllCachedResponses()
        WatchProgressStore.shared.clearAll()
    }
}

// ─────────────────────────────────────────────
// MARK: – Data Models
// ─────────────────────────────────────────────
struct VideoItem: Identifiable, Hashable, Codable {
    let id: String
    let title: String
    let imageUrl: String
    let type: String
}

struct EpisodeItem: Identifiable, Hashable {
    let id: String
    let title: String
    let url: String
    let url720: String   // نفس url الأساسي (الموقع لا يوفر 720 للمسلسلات)
    let url1080: String
    let url360: String
    let subtitleUrl: String
    let subtitleVttUrl: String

    // استخرج رقم الموسم من العنوان مثل S01 أو Season 1
    var season: String {
        let ns = title as NSString
        // نمط S01Exx
        if let rx = try? NSRegularExpression(pattern: #"[Ss](\d{1,2})[Ee]\d"#),
           let m = rx.firstMatch(in: title, range: NSRange(location: 0, length: ns.length)) {
            let n = Int(ns.substring(with: m.range(at: 1))) ?? 1
            return "الموسم \(n)"
        }
        // نمط Season 1
        if let rx = try? NSRegularExpression(pattern: #"[Ss]eason\s*(\d+)"#),
           let m = rx.firstMatch(in: title, range: NSRange(location: 0, length: ns.length)) {
            let n = Int(ns.substring(with: m.range(at: 1))) ?? 1
            return "الموسم \(n)"
        }
        return "الموسم 1"
    }
}

struct MediaDetails {
    var title: String = ""
    var imageUrl: String = ""
    var year: String = ""
    var genre: String = ""
    var rating: String = ""
    var runtime: String = ""
    var synopsis: String = ""
    var isMovie: Bool = true
    var movieUrl: String = ""
    var movieUrl720: String = ""
    var movieUrl1080: String = ""
    var movieUrl360: String = ""
    var movieSubtitleUrl: String = ""
    var movieSubtitleVttUrl: String = ""
    var episodes: [EpisodeItem] = []

    // تجميع الحلقات حسب الموسم مع إعادة الترتيب
    var seasonsDict: [String: [EpisodeItem]] {
        Dictionary(grouping: episodes, by: { $0.season })
    }
    var sortedSeasons: [String] {
        seasonsDict.keys.sorted {
            let n1 = Int($0.filter(\.isNumber)) ?? 0
            let n2 = Int($1.filter(\.isNumber)) ?? 0
            return n1 < n2
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Watch Progress Store
// ─────────────────────────────────────────────
struct WatchProgress: Codable, Identifiable {
    var id: String { itemId }
    var itemId: String
    var title: String
    var imageUrl: String
    var episodeId: String
    var episodeTitle: String
    var progressSeconds: Double
    var durationSeconds: Double
    var updatedAt: Date

    var videoUrl: String = ""
    var videoUrl720: String = ""
    var videoUrl1080: String = ""
    var videoUrl360: String = ""
    var subtitleUrl: String = ""
    var subtitleVttUrl: String = ""
}

class WatchProgressStore: ObservableObject {
    static let shared = WatchProgressStore()
    private let key = "UTanWatchProgress_v4"
    @Published var allProgress: [String: WatchProgress] = [:]
    private init() { load() }

    func save(itemId: String, title: String, imageUrl: String,
              episodeId: String, episodeTitle: String,
              progress: Double, duration: Double,
              videoUrl: String, videoUrl720: String,
              videoUrl1080: String, videoUrl360: String,
              subUrl: String, subVttUrl: String) {
        let rec = WatchProgress(
            itemId: itemId, title: title, imageUrl: imageUrl,
            episodeId: episodeId, episodeTitle: episodeTitle,
            progressSeconds: progress, durationSeconds: duration,
            updatedAt: Date(),
            videoUrl: videoUrl, videoUrl720: videoUrl720,
            videoUrl1080: videoUrl1080, videoUrl360: videoUrl360,
            subtitleUrl: subUrl, subtitleVttUrl: subVttUrl)
        allProgress[itemId] = rec
        persist()
    }
    func remove(itemId: String) { allProgress.removeValue(forKey: itemId); persist() }
    func clearAll()              { allProgress.removeAll(); persist() }
    func progress(for id: String) -> WatchProgress? { allProgress[id] }
    var recent: [WatchProgress] { allProgress.values.sorted { $0.updatedAt > $1.updatedAt } }
    private func load() {
        guard let d = UserDefaults.standard.data(forKey: key),
              let dec = try? JSONDecoder().decode([String: WatchProgress].self, from: d)
        else { return }
        allProgress = dec
    }
    private func persist() {
        if let d = try? JSONEncoder().encode(allProgress) {
            UserDefaults.standard.set(d, forKey: key)
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Favorites Store
// ─────────────────────────────────────────────
class FavoritesStore: ObservableObject {
    static let shared = FavoritesStore()
    private let key = "UTanFavorites_v2"
    @Published var items: [VideoItem] = []
    private init() { load() }
    func toggle(item: VideoItem) {
        if let i = items.firstIndex(where: { $0.id == item.id }) { items.remove(at: i) }
        else { items.insert(item, at: 0) }
        persist()
    }
    func isFavorite(_ id: String) -> Bool { items.contains(where: { $0.id == id }) }
    private func load() {
        if let d = UserDefaults.standard.data(forKey: key),
           let dec = try? JSONDecoder().decode([VideoItem].self, from: d) { items = dec }
    }
    private func persist() {
        if let d = try? JSONEncoder().encode(items) { UserDefaults.standard.set(d, forKey: key) }
    }
}

// ─────────────────────────────────────────────
// MARK: – Download Manager
// ─────────────────────────────────────────────
struct DownloadTaskItem: Identifiable, Codable {
    let id: String
    let title: String
    let imageUrl: String
    let isMovie: Bool
    var videoUrl: String
    var subtitleUrl: String
    var progress: Double = 0.0
    var isCompleted: Bool = false
    var localVideoPath: String?
}

class DownloadManager: NSObject, ObservableObject, URLSessionDownloadDelegate {
    static let shared = DownloadManager()
    private let key = "UTanDownloads_v2"
    @Published var activeDownloads: [DownloadTaskItem] = []
    private var session: URLSession!
    private var taskMap: [Int: String] = [:]

    private override init() {
        super.init()
        let cfg = URLSessionConfiguration.background(withIdentifier: "com.mustaqil.utan.bg")
        session = URLSession(configuration: cfg, delegate: self, delegateQueue: nil)
        load()
    }
    func startDownload(item: VideoItem, isMovie: Bool, vUrl: String, sUrl: String) {
        guard !activeDownloads.contains(where: { $0.id == item.id }) else { return }
        let dl = DownloadTaskItem(id: item.id, title: item.title, imageUrl: item.imageUrl,
                                  isMovie: isMovie, videoUrl: vUrl, subtitleUrl: sUrl)
        DispatchQueue.main.async { self.activeDownloads.append(dl); self.persist() }
        if let url = URL(string: vUrl) {
            let t = session.downloadTask(with: url)
            taskMap[t.taskIdentifier] = item.id
            t.resume()
        }
    }
    func cancel(id: String) {
        DispatchQueue.main.async { self.activeDownloads.removeAll(where: { $0.id == id }); self.persist() }
    }
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didWriteData _: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64) {
        guard let id = taskMap[downloadTask.taskIdentifier], totalBytesExpectedToWrite > 0 else { return }
        let p = Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
        DispatchQueue.main.async {
            if let i = self.activeDownloads.firstIndex(where: { $0.id == id }) { self.activeDownloads[i].progress = p }
        }
    }
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didFinishDownloadingTo location: URL) {
        guard let id = taskMap[downloadTask.taskIdentifier] else { return }
        let dest = FileManager.default.temporaryDirectory.appendingPathComponent(id + ".mp4")
        try? FileManager.default.removeItem(at: dest)
        try? FileManager.default.moveItem(at: location, to: dest)
        DispatchQueue.main.async {
            if let i = self.activeDownloads.firstIndex(where: { $0.id == id }) {
                self.activeDownloads[i].isCompleted  = true
                self.activeDownloads[i].localVideoPath = dest.path
                self.persist()
                UISaveVideoAtPathToSavedPhotosAlbum(dest.path, nil, nil, nil)
            }
        }
    }
    private func load() {
        if let d = UserDefaults.standard.data(forKey: key),
           let dec = try? JSONDecoder().decode([DownloadTaskItem].self, from: d) { activeDownloads = dec }
    }
    private func persist() {
        if let d = try? JSONEncoder().encode(activeDownloads) { UserDefaults.standard.set(d, forKey: key) }
    }
}

// ─────────────────────────────────────────────
// MARK: – Site Categories
// ─────────────────────────────────────────────
struct SiteCategory: Identifiable {
    let id: Int
    let remoteId: Int
    let isTag: Bool
    let nameAr: String
    let nameEn: String
    init(id: Int, remoteId: Int? = nil, isTag: Bool = false, nameAr: String, nameEn: String) {
        self.id = id; self.remoteId = remoteId ?? id
        self.isTag = isTag; self.nameAr = nameAr; self.nameEn = nameEn
    }
}

let SITE_CATEGORIES: [SiteCategory] = [
    SiteCategory(id: 0,    nameAr: "أفلام إنجليزية",       nameEn: "English Movies"),
    SiteCategory(id: 1,    nameAr: "مسلسلات أجنبية",       nameEn: "TV Series"),
    SiteCategory(id: 2,    nameAr: "أنمي",                  nameEn: "Anime Series"),
    SiteCategory(id: 3,    nameAr: "بوليوود",               nameEn: "Bollywood Movies"),
    SiteCategory(id: 4,    nameAr: "مسلسلات عربية",        nameEn: "Arabic Series"),
    SiteCategory(id: 5,    nameAr: "مسلسلات آسيوية",       nameEn: "Asian Series"),
    SiteCategory(id: 6,    nameAr: "أفلام آسيوية",         nameEn: "Asian Movies"),
    SiteCategory(id: 7,    nameAr: "أفلام عربية",          nameEn: "Arabic Movies"),
    SiteCategory(id: 8,    nameAr: "مسلسلات بوليوود",      nameEn: "Bollywood Series"),
    SiteCategory(id: 9,    nameAr: "أفلام أنمي",           nameEn: "Anime Movies"),
    SiteCategory(id: 10,   nameAr: "أفلام مكتب الصندوق",   nameEn: "US Box Office"),
    SiteCategory(id: 13,   nameAr: "سينما عربية",          nameEn: "Arabic Cinemas"),
    SiteCategory(id: 14,   nameAr: "أفلام تركية",          nameEn: "Turkish Movies"),
    SiteCategory(id: 15,   nameAr: "مسلسلات تركية",        nameEn: "Turkish Series"),
    SiteCategory(id: 16,   nameAr: "أفلام كرتون",          nameEn: "Cartoon Movies"),
    SiteCategory(id: 17,   nameAr: "مسلسلات كرتون",        nameEn: "Cartoon Series"),
    SiteCategory(id: 18,   nameAr: "أفلام أجنبية",         nameEn: "Foreign Movies"),
    SiteCategory(id: 20,   nameAr: "مسلسلات مدبلجة عربي",  nameEn: "Arabic Dubbed Series"),
    SiteCategory(id: 21,   nameAr: "أفلام مدبلجة عربي",   nameEn: "Arabic Dubbed Movies"),
    SiteCategory(id: 1014, nameAr: "أفلام كردية",          nameEn: "Kurdish Movies"),
    SiteCategory(id: 1015, nameAr: "مسلسلات كردية",        nameEn: "Kurdish Series"),
    SiteCategory(id: 1022, nameAr: "أنمي عربي",            nameEn: "Arabic Anime"),
    SiteCategory(id: 1029, nameAr: "أنمي مدبلج إنجليزي",  nameEn: "English Dubbed Anime"),
    SiteCategory(id: 44,  remoteId: 44, isTag: true, nameAr: "نتفليكس",           nameEn: "Netflix"),
    SiteCategory(id: 9014,remoteId: 14, isTag: true, nameAr: "عالم مارفل",        nameEn: "Marvel"),
    SiteCategory(id: 73,  remoteId: 73, isTag: true, nameAr: "اتش بي او ماكس",   nameEn: "HBO Max"),
    SiteCategory(id: 72,  remoteId: 72, isTag: true, nameAr: "ديزني بلاس",        nameEn: "Disney+"),
    SiteCategory(id: 9018,remoteId: 18, isTag: true, nameAr: "للأطفال",           nameEn: "For Kids"),
]

// ─────────────────────────────────────────────
// MARK: – Image URL helper
// ─────────────────────────────────────────────
/// تحوّل روابط الموقع لصورة بجودة عالية
func optimizeImageUrl(_ raw: String, w: Int = 320, h: Int = 512) -> String {
    guard !raw.isEmpty else { return raw }
    var url = raw
    // الرابط يبدأ بـ image/s3 → نضيف الدومين
    if !url.hasPrefix("http") { url = "https://movie.vodu.me/" + url }
    // إزالة معاملات الحجم القديمة من السلسلة &w=xxx أو ?w=xxx
    url = url.replacingOccurrences(of: #"[&?]w=\d+"#,  with: "", options: .regularExpression)
    url = url.replacingOccurrences(of: #"[&?]h=\d+"#,  with: "", options: .regularExpression)
    url = url.replacingOccurrences(of: #"[&?]q=\d+"#,  with: "", options: .regularExpression)
    url = url.replacingOccurrences(of: #"[&?]crop-to-fit"#, with: "", options: .regularExpression)
    // تنظيف ? أو & زائدة في النهاية
    while url.hasSuffix("&") || url.hasSuffix("?") { url = String(url.dropLast()) }
    let sep = url.contains("?") ? "&" : "?"
    return "\(url)\(sep)w=\(w)&h=\(h)&crop-to-fit&q=80"
}

// ─────────────────────────────────────────────
// MARK: – Main Scraper
// ─────────────────────────────────────────────
class MovieScraper: ObservableObject {
    @Published var heroItems: [VideoItem] = []
    @Published var categories: [(name: String, items: [VideoItem])] = []
    @Published var isLoading = false

    let baseUrl = "https://movie.vodu.me/"
    private let ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

    // الأقسام التي تُجلب في الصفحة الرئيسية (tag ID مطابق للموقع)
    let homeSections: [(name: String, tagId: Int)] = [
        ("Ramadan 2026",       332),
        ("Featured",            79),
        ("Latest Movies",       83),
        ("Anime Spring 2026",  339),
        ("Latest Series",       84),
        ("Turkish Series",     243),
        ("Korean Drama",        42),
        ("Netflix",             44),
        ("Apple TV+",           62),
        ("Disney+",             72),
        ("HBO Max",             73),
        ("Action Movies",       69),
        ("Spanish",             94),
        ("Documentaries",      142),
        ("Kids TV",             18),
    ]

    // ── fetchHome ────────────────────────────────────────────────────────────
    func fetchHome() {
        guard let url = URL(string: baseUrl + "index.php") else { return }
        isLoading = true
        var req = URLRequest(url: url)
        req.setValue(ua, forHTTPHeaderField: "User-Agent")

        URLSession.shared.dataTask(with: req) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { self.isLoading = false }
                return
            }
            let carouselItems = Self.parseCarousel(html: html, base: self.baseUrl)

            DispatchQueue.main.async { self.heroItems = carouselItems }

            // جلب الأقسام بالتوازي
            let group  = DispatchGroup()
            var results: [(idx: Int, name: String, items: [VideoItem])] = []
            let lock = NSLock()

            for (i, section) in self.homeSections.enumerated() {
                group.enter()
                self.fetchCategory(typeId: section.tagId, page: 1, useTag: true) { items, _ in
                    if !items.isEmpty {
                        lock.lock()
                        results.append((idx: i, name: section.name, items: Array(items.prefix(12))))
                        lock.unlock()
                    }
                    group.leave()
                }
            }

            group.notify(queue: .main) {
                // ترتيب حسب الفهرس الأصلي
                let sorted = results.sorted { $0.idx < $1.idx }.map { (name: $0.name, items: $0.items) }
                var all: [(name: String, items: [VideoItem])] = []
                if !carouselItems.isEmpty {
                    all.append(("الرائج الآن", Array(carouselItems.prefix(10))))
                }
                all.append(contentsOf: sorted)
                self.categories = all
                self.isLoading  = false
            }
        }.resume()
    }

    // ── fetchCategory ────────────────────────────────────────────────────────
    func fetchCategory(typeId: Int, page: Int = 1, useTag: Bool = false,
                       completion: @escaping ([VideoItem], Bool) -> Void) {
        let urlStr = useTag
            ? "\(baseUrl)?do=list&tag=\(typeId)&page=\(page)"
            : "\(baseUrl)index.php?do=list&type=\(typeId)&page=\(page)"
        guard let url = URL(string: urlStr) else { completion([], false); return }
        var req = URLRequest(url: url)
        req.setValue(ua, forHTTPHeaderField: "User-Agent")
        URLSession.shared.dataTask(with: req) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([], false) }; return
            }
            let items   = Self.parseListPage(html: html, base: self.baseUrl)
            let hasMore = html.contains("class=\"next\"") || html.contains("»")
            DispatchQueue.main.async { completion(items, hasMore) }
        }.resume()
    }

    // ── search ───────────────────────────────────────────────────────────────
    func search(query: String, completion: @escaping ([VideoItem]) -> Void) {
        let enc = query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? query
        guard let url = URL(string: "\(baseUrl)index.php?do=list&title=\(enc)") else {
            completion([]); return
        }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([]) }; return
            }
            DispatchQueue.main.async { completion(Self.parseListPage(html: html, base: self.baseUrl)) }
        }.resume()
    }

    // ── fetchDetails ─────────────────────────────────────────────────────────
    func fetchDetails(id: String, completion: @escaping (MediaDetails) -> Void) {
        guard let url = URL(string: "\(baseUrl)index.php?do=view&type=post&id=\(id)") else { return }
        var req = URLRequest(url: url)
        req.setValue(ua, forHTTPHeaderField: "User-Agent")
        URLSession.shared.dataTask(with: req) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion(MediaDetails()) }; return
            }
            let d = Self.parseDetails(html: html, base: self.baseUrl)
            DispatchQueue.main.async { completion(d) }
        }.resume()
    }

    // ═════════════════════════════════════════
    // MARK: – HTML Parsers
    // ═════════════════════════════════════════

    // ── Carousel (صفحة رئيسية – البانر) ────────────────────────────────────
    /// يستخرج عناصر قسم <div class="item"> من الكاروسيل
    static func parseCarousel(html: String, base: String) -> [VideoItem] {
        var items: [VideoItem] = []
        // نمط: <a href="index.php?do=view&type=post&id=XXX"><img src="..." alt="TITLE">
        let pat = #"<a href=\"index\.php\?do=view&amp;type=post&id=(\d+)\"><img src=\"([^\"]+)\"[^>]*alt=\"([^\"]*)\""#
        guard let rx = try? NSRegularExpression(pattern: pat, options: []) else { return items }
        let ns = html as NSString
        _ = ns // silence unused warning
        for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
            guard m.numberOfRanges == 4 else { continue }
            let id    = ns.substring(with: m.range(at: 1))
            var img   = ns.substring(with: m.range(at: 2))
            let title = ns.substring(with: m.range(at: 3))
            if !img.hasPrefix("http") { img = base + img }
            let opt = optimizeImageUrl(img, w: 750, h: 420)
            if !items.contains(where: { $0.id == id }) {
                items.append(VideoItem(id: id, title: title, imageUrl: opt, type: "post"))
            }
        }
        // fallback بدون &amp;
        if items.isEmpty {
            let pat2 = #"<a href=\"index\.php\?do=view&type=post&id=(\d+)\"><img src=\"([^\"]+)\"[^>]*alt=\"([^\"]*)\""#
            if let rx2 = try? NSRegularExpression(pattern: pat2, options: []) {
                let ns2 = html as NSString
                for m in rx2.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                    guard m.numberOfRanges == 4 else { continue }
                    let id    = ns2.substring(with: m.range(at: 1))
                    var img   = ns2.substring(with: m.range(at: 2))
                    let title = ns2.substring(with: m.range(at: 3))
                    if !img.hasPrefix("http") { img = base + img }
                    let opt = optimizeImageUrl(img, w: 750, h: 420)
                    if !items.contains(where: { $0.id == id }) {
                        items.append(VideoItem(id: id, title: title, imageUrl: opt, type: "post"))
                    }
                }
            }
        }
        return items
    }

    // ── List Page ────────────────────────────────────────────────────────────
    /// يستخرج عناصر <div class="itemx"> من صفحات القوائم والصفحة الرئيسية
    static func parseListPage(html: String, base: String) -> [VideoItem] {
        var items: [VideoItem] = []
        // النمط الجديد: href="index.php?do=view&type=post&id=XXX" → img → mytitle
        let pat = #"href=\"index\.php\?do=view&(?:amp;)?type=post&(?:amp;)?id=(\d+)\">\s*<img src=\"([^\"]+)\"[^>]*>\s*<div class=\"mytitle\">([^<]+)</div>"#
        if let rx = try? NSRegularExpression(pattern: pat, options: [.dotMatchesLineSeparators]) {
            let ns = html as NSString
            for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                guard m.numberOfRanges == 4 else { continue }
                let id    = ns.substring(with: m.range(at: 1))
                var img   = ns.substring(with: m.range(at: 2))
                let title = ns.substring(with: m.range(at: 3)).trimmingCharacters(in: .whitespacesAndNewlines)
                if !img.hasPrefix("http") { img = base + img }
                let opt = optimizeImageUrl(img)
                if !items.contains(where: { $0.id == id }) {
                    items.append(VideoItem(id: id, title: title, imageUrl: opt, type: "post"))
                }
            }
        }
        return items
    }

    // ── Details ──────────────────────────────────────────────────────────────
    static func parseDetails(html: String, base: String) -> MediaDetails {
        var d = MediaDetails()

        func first(_ pat: String, in text: String, opts: NSRegularExpression.Options = []) -> String? {
            guard let rx = try? NSRegularExpression(pattern: pat, options: opts),
                  let m  = rx.firstMatch(in: text, range: NSRange(text.startIndex..., in: text)),
                  m.numberOfRanges >= 2,
                  let r  = Range(m.range(at: 1), in: text)
            else { return nil }
            return String(text[r]).trimmingCharacters(in: .whitespacesAndNewlines)
        }

        d.title   = first(#"<h1>(.*?)</h1>"#, in: html) ?? ""
        d.year    = first(#"<span>Year:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.genre   = first(#"<span>Genre:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.rating  = first(#"<span>IMdB Rating:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.runtime = first(#"<span>Runtime:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.synopsis = first(#"<h3>Synopsis:</h3>.*?<h4>(.*?)</h4>"#, in: html,
                           opts: [.dotMatchesLineSeparators]) ?? ""

        // صورة
        if let img = first(#"<img src=\"([^\"]+)\" class=\"img-responsive\""#, in: html) {
            let abs = img.hasPrefix("http") ? img : base + img
            d.imageUrl = optimizeImageUrl(abs, w: 800, h: 1200)
        }

        // ── حلقات المسلسل ────────────────────────────────────────────────────
        // النمط الفعلي الموجود في الصفحة (بدون url720):
        //   data-id="XXX" data-title="..." data-url="..." data-url360="..." data-url1080="..." data-srt="..." data-webvtt="..."
        var episodes: [EpisodeItem] = []
        let blockPat = #"<li class=\"episodeitem\">(.*?)</li>"#
        if let bRx = try? NSRegularExpression(pattern: blockPat, options: [.dotMatchesLineSeparators]) {
            let ns = html as NSString
            for bm in bRx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                guard bm.numberOfRanges >= 2, let br = Range(bm.range(at: 1), in: html) else { continue }
                let blk = String(html[br])

                func attr(_ name: String) -> String {
                    let p = "data-\(name)=\"([^\"]*)\""
                    guard let rx = try? NSRegularExpression(pattern: p),
                          let m  = rx.firstMatch(in: blk, range: NSRange(blk.startIndex..., in: blk)),
                          m.numberOfRanges >= 2,
                          let r  = Range(m.range(at: 1), in: blk)
                    else { return "" }
                    return String(blk[r])
                }

                let epId   = attr("id")
                guard !epId.isEmpty else { continue }
                let epUrl  = attr("url")
                guard !epUrl.isEmpty else { continue }

                let epTitle = attr("title")
                let ep360   = attr("url360")
                let ep1080  = attr("url1080")
                let epSrt   = attr("srt")
                let epVtt   = attr("webvtt")

                episodes.append(EpisodeItem(
                    id: epId,
                    title: epTitle.isEmpty ? "الحلقة \(episodes.count + 1)" : epTitle,
                    url: epUrl,
                    url720: epUrl,   // الموقع لا يوفر 720p للمسلسلات
                    url1080: ep1080,
                    url360:  ep360,
                    subtitleUrl:    epSrt,
                    subtitleVttUrl: epVtt
                ))
            }
        }

        if episodes.isEmpty {
            // ── فيلم ──────────────────────────────────────────────────────
            d.isMovie = true
            // نمط الفيلم (بدون url720 أيضاً)
            let moviePat = #"data-url=\"([^\"]+)\"[^>]*data-url360=\"([^\"]*)\""# +
                           #"[^>]*data-url1080=\"([^\"]*)\""# +
                           #"[^>]*data-srt=\"([^\"]*)\""# +
                           #"[^>]*data-webvtt=\"([^\"]*)\""#
            if let rx = try? NSRegularExpression(pattern: moviePat, options: [.dotMatchesLineSeparators]),
               let m  = rx.firstMatch(in: html, range: NSRange(html.startIndex..., in: html)) {
                func str(_ i: Int) -> String {
                    guard m.range(at: i).location != NSNotFound,
                          let r = Range(m.range(at: i), in: html) else { return "" }
                    return String(html[r])
                }
                d.movieUrl           = str(1)
                d.movieUrl360        = str(2)
                d.movieUrl1080       = str(3)
                d.movieUrl720        = str(1)   // fallback
                d.movieSubtitleUrl   = str(4)
                d.movieSubtitleVttUrl = str(5)
            }
        } else {
            d.isMovie  = false
            d.episodes = episodes
        }
        return d
    }
}

// ─────────────────────────────────────────────
// MARK: – Color Hex Extension
// ─────────────────────────────────────────────
extension Color {
    init(hex: String) {
        let h = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: h).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch h.count {
        case 3: (a,r,g,b) = (255,(int>>8)*17,(int>>4&0xF)*17,(int&0xF)*17)
        case 6: (a,r,g,b) = (255,int>>16,int>>8&0xFF,int&0xFF)
        case 8: (a,r,g,b) = (int>>24,int>>16&0xFF,int>>8&0xFF,int&0xFF)
        default:(a,r,g,b) = (255,255,255,255)
        }
        self.init(.sRGB,
                  red:   Double(r)/255,
                  green: Double(g)/255,
                  blue:  Double(b)/255,
                  opacity: Double(a)/255)
    }
}
"""
with open("UTan/UTan/Scraper.swift", "w", encoding="utf-8") as f:
    f.write(scraper_swift)
print("✅ Scraper.swift كُتب")

# ─── 5. SubtitleParser.swift ──────────────────────────────────────────────────
sub_swift = r"""import Foundation

struct SubtitleCue: Identifiable {
    let id  = UUID()
    let startTime: TimeInterval
    let endTime: TimeInterval
    let text: String
}

class SubtitleParser {
    static func parse(url: String, completion: @escaping ([SubtitleCue]) -> Void) {
        guard !url.isEmpty else { completion([]); return }
        var clean = url
        if !clean.hasPrefix("http") { clean = "https://movie.vodu.me/" + clean }
        guard let urlObj = URL(string: clean) else { completion([]); return }

        URLSession.shared.dataTask(with: urlObj) { data, _, _ in
            guard let data = data else { DispatchQueue.main.async { completion([]) }; return }
            var text: String?
            for enc: String.Encoding in [.utf8, .isoLatin1, .windowsCP1252] {
                if let s = String(data: data, encoding: enc) { text = s; break }
            }
            guard let src = text else { DispatchQueue.main.async { completion([]) }; return }
            let cues = src.contains("WEBVTT") ? parseVTT(src) : parseSRT(src)
            DispatchQueue.main.async { completion(cues) }
        }.resume()
    }

    private static func parseSRT(_ s: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let blocks = s.components(separatedBy: "\n\n")
        for block in blocks {
            let lines = block.components(separatedBy: .newlines)
                             .map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
                             .filter { !$0.isEmpty }
            guard lines.count >= 3 else { continue }
            let times = lines[1].components(separatedBy: " --> ")
            guard times.count == 2,
                  let s = srtTime(times[0]),
                  let e = srtTime(times[1]) else { continue }
            let txt = lines[2...].joined(separator: "\n")
                      .replacingOccurrences(of: #"<[^>]+>"#, with: "", options: .regularExpression)
                      .trimmingCharacters(in: .whitespacesAndNewlines)
            if !txt.isEmpty { cues.append(SubtitleCue(startTime: s, endTime: e, text: txt)) }
        }
        return cues
    }

    private static func parseVTT(_ s: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let lines = s.components(separatedBy: .newlines)
        var i = 0
        while i < lines.count {
            let line = lines[i].trimmingCharacters(in: .whitespacesAndNewlines)
            if line.contains("-->") {
                let parts = line.components(separatedBy: "-->")
                guard parts.count == 2,
                      let sv = vttTime(parts[0]),
                      let ev = vttTime(parts[1]) else { i += 1; continue }
                var textLines: [String] = []
                i += 1
                while i < lines.count {
                    let l = lines[i].trimmingCharacters(in: .whitespacesAndNewlines)
                    if l.isEmpty { break }
                    textLines.append(l)
                    i += 1
                }
                let txt = textLines.joined(separator: "\n")
                          .replacingOccurrences(of: #"<[^>]+>"#, with: "", options: .regularExpression)
                          .trimmingCharacters(in: .whitespacesAndNewlines)
                if !txt.isEmpty { cues.append(SubtitleCue(startTime: sv, endTime: ev, text: txt)) }
            }
            i += 1
        }
        return cues
    }

    private static func srtTime(_ s: String) -> TimeInterval? {
        let p = s.trimmingCharacters(in: .whitespacesAndNewlines).components(separatedBy: ",")
        guard p.count == 2, let ms = Double(p[1]) else { return nil }
        let hms = p[0].components(separatedBy: ":")
        guard hms.count == 3,
              let h  = Double(hms[0]),
              let m  = Double(hms[1]),
              let sc = Double(hms[2]) else { return nil }
        return h*3600 + m*60 + sc + ms/1000
    }

    private static func vttTime(_ s: String) -> TimeInterval? {
        let clean = s.trimmingCharacters(in: .whitespacesAndNewlines)
        let parts = clean.components(separatedBy: ":")
        var h = 0.0, m = 0.0, sec = 0.0
        if parts.count == 3 {
            h = Double(parts[0]) ?? 0
            m = Double(parts[1]) ?? 0
            let sp = parts[2].components(separatedBy: "."); sec = Double(sp[0]) ?? 0
            if sp.count == 2 { sec += (Double(sp[1]) ?? 0)/1000 }
        } else if parts.count == 2 {
            m = Double(parts[0]) ?? 0
            let sp = parts[1].components(separatedBy: "."); sec = Double(sp[0]) ?? 0
            if sp.count == 2 { sec += (Double(sp[1]) ?? 0)/1000 }
        } else { return nil }
        return h*3600 + m*60 + sec
    }
}
"""
with open("UTan/UTan/SubtitleParser.swift", "w", encoding="utf-8") as f:
    f.write(sub_swift)
print("✅ SubtitleParser.swift كُتب")

# ─── 6. CustomPlayer.swift (إزالة weak وإضافة UIKit) ─────────────────────────
player_swift = r"""import SwiftUI
import AVKit
import AVFoundation
import UIKit

// ─────────────────────────────────────────────
// MARK: – Enums
// ─────────────────────────────────────────────
enum VideoQuality: String, CaseIterable, Identifiable {
    case auto  = "تلقائي"
    case q360  = "360p"
    case q1080 = "1080p"
    var id: String { rawValue }
}

enum VideoFitMode: String, CaseIterable, Identifiable {
    case fit  = "ملاءمة"
    case fill = "تمديد"
    case zoom = "قص"
    var id: String { rawValue }
    var gravity: AVLayerVideoGravity {
        switch self {
        case .fit:  return .resizeAspect
        case .fill: return .resize
        case .zoom: return .resizeAspectFill
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Video Player UIViewController Wrapper
// ─────────────────────────────────────────────
struct VideoPlayerView: UIViewControllerRepresentable {
    let player: AVPlayer
    let gravity: AVLayerVideoGravity
    let onTap: () -> Void
    let onLongPressBegan: () -> Void
    let onLongPressEnded: () -> Void
    let onDoubleTap: (Bool) -> Void   // isRightHalf

    func makeUIViewController(context: Context) -> AVPlayerViewController {
        let vc = AVPlayerViewController()
        vc.player = player
        vc.showsPlaybackControls = false
        vc.videoGravity = gravity

        // Overlay لاستقبال الإيماءات
        let overlay = UIView()
        overlay.backgroundColor = .clear
        overlay.translatesAutoresizingMaskIntoConstraints = false
        vc.contentOverlayView?.addSubview(overlay)
        if let parent = vc.contentOverlayView {
            NSLayoutConstraint.activate([
                overlay.leadingAnchor.constraint(equalTo: parent.leadingAnchor),
                overlay.trailingAnchor.constraint(equalTo: parent.trailingAnchor),
                overlay.topAnchor.constraint(equalTo: parent.topAnchor),
                overlay.bottomAnchor.constraint(equalTo: parent.bottomAnchor),
            ])
        }

        let singleTap  = UITapGestureRecognizer(target: context.coordinator,
                                                action: #selector(Coordinator.handleTap))
        singleTap.numberOfTapsRequired = 1

        let doubleTap  = UITapGestureRecognizer(target: context.coordinator,
                                                action: #selector(Coordinator.handleDouble(_:)))
        doubleTap.numberOfTapsRequired = 2
        singleTap.require(toFail: doubleTap)   // لا تنفّذ singleTap إذا كان double

        let longPress  = UILongPressGestureRecognizer(target: context.coordinator,
                                                      action: #selector(Coordinator.handleLong(_:)))
        longPress.minimumPressDuration = 0.4

        overlay.addGestureRecognizer(singleTap)
        overlay.addGestureRecognizer(doubleTap)
        overlay.addGestureRecognizer(longPress)

        // شعار ماء
        if let img = UIImage(named: "logo") {
            let wm = UIImageView(image: img)
            wm.alpha = 0.3
            wm.contentMode = .scaleAspectFit
            wm.translatesAutoresizingMaskIntoConstraints = false
            vc.view.addSubview(wm)
            NSLayoutConstraint.activate([
                wm.leadingAnchor.constraint(equalTo: vc.view.leadingAnchor, constant: 14),
                wm.topAnchor.constraint(equalTo: vc.view.safeAreaLayoutGuide.topAnchor, constant: 10),
                wm.widthAnchor.constraint(equalToConstant: 80),
                wm.heightAnchor.constraint(equalToConstant: 32),
            ])
        }
        return vc
    }

    func updateUIViewController(_ vc: AVPlayerViewController, context: Context) {
        vc.videoGravity = gravity
    }

    func makeCoordinator() -> Coordinator {
        Coordinator(onTap: onTap, onLongBegan: onLongPressBegan,
                    onLongEnded: onLongPressEnded, onDouble: onDoubleTap)
    }

    class Coordinator: NSObject {
        let onTap: () -> Void
        let onLongBegan: () -> Void
        let onLongEnded: () -> Void
        let onDouble: (Bool) -> Void
        init(onTap: @escaping () -> Void, onLongBegan: @escaping () -> Void,
             onLongEnded: @escaping () -> Void, onDouble: @escaping (Bool) -> Void) {
            self.onTap = onTap; self.onLongBegan = onLongBegan
            self.onLongEnded = onLongEnded; self.onDouble = onDouble
        }
        @objc func handleTap()   { onTap() }
        @objc func handleDouble(_ g: UITapGestureRecognizer) {
            let x = g.location(in: g.view).x
            onDouble(x > (g.view?.bounds.width ?? 0) / 2)
        }
        @objc func handleLong(_ g: UILongPressGestureRecognizer) {
            switch g.state {
            case .began:                          onLongBegan()
            case .ended, .cancelled, .failed:     onLongEnded()
            default: break
            }
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Seek Feedback View
// ─────────────────────────────────────────────
struct SeekFeedbackView: View {
    let isRight: Bool
    var body: some View {
        HStack(spacing: 8) {
            Image(systemName: isRight ? "goforward.10" : "gobackward.10")
                .font(.system(size: 42, weight: .medium))
            Text(isRight ? "+10" : "-10")
                .font(.system(size: 22, weight: .semibold))
        }
        .foregroundColor(.white)
        .padding(.horizontal, 22).padding(.vertical, 12)
        .background(.ultraThinMaterial, in: Capsule())
    }
}

// ─────────────────────────────────────────────
// MARK: – Episode List Panel (يرتفع بالإصبع)
// ─────────────────────────────────────────────
struct EpisodeListPanel: View {
    let episodes: [EpisodeItem]
    let currentEpisodeId: String
    let onSelect: (EpisodeItem) -> Void

    @GestureState private var dragOffset: CGFloat = 0
    @Binding var isShown: Bool

    var body: some View {
        VStack(spacing: 0) {
            // مقبض السحب
            Capsule()
                .fill(Color.white.opacity(0.4))
                .frame(width: 44, height: 5)
                .padding(.top, 10).padding(.bottom, 8)

            Text("قائمة الحلقات")
                .font(.system(size: 18, weight: .bold))
                .foregroundColor(.white)
                .padding(.bottom, 10)

            Divider().background(Color.white.opacity(0.2))

            ScrollViewReader { proxy in
                ScrollView(showsIndicators: false) {
                    LazyVStack(spacing: 0) {
                        ForEach(episodes) { ep in
                            Button {
                                onSelect(ep)
                                isShown = false
                            } label: {
                                HStack(spacing: 14) {
                                    Image(systemName: ep.id == currentEpisodeId
                                          ? "play.circle.fill" : "play.circle")
                                        .font(.system(size: 22))
                                        .foregroundColor(ep.id == currentEpisodeId ? UT_RED : .gray)

                                    Text(ep.title)
                                        .font(.system(size: 15, weight: ep.id == currentEpisodeId ? .bold : .regular))
                                        .foregroundColor(ep.id == currentEpisodeId ? .white : Color(.lightGray))
                                        .lineLimit(2)
                                        .multilineTextAlignment(.leading)

                                    Spacer()
                                }
                                .padding(.horizontal, 20)
                                .padding(.vertical, 14)
                                .background(ep.id == currentEpisodeId
                                            ? Color.white.opacity(0.1) : Color.clear)
                            }
                            Divider().background(Color.white.opacity(0.08)).padding(.leading, 56)
                        }
                    }
                }
                .onAppear {
                    if let cur = episodes.first(where: { $0.id == currentEpisodeId }) {
                        DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
                            withAnimation { proxy.scrollTo(cur.id, anchor: .center) }
                        }
                    }
                }
            }
        }
        .background(Color(red: 0.07, green: 0.04, blue: 0.12).opacity(0.97))
        .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
        .shadow(color: .black.opacity(0.5), radius: 20, x: 0, y: -4)
        .offset(y: dragOffset)
        .gesture(
            DragGesture()
                .updating($dragOffset) { val, state, _ in
                    if val.translation.height > 0 { state = val.translation.height }
                }
                .onEnded { val in
                    if val.translation.height > 120 { isShown = false }
                }
        )
        .transition(.move(edge: .bottom).combined(with: .opacity))
    }
}

// ─────────────────────────────────────────────
// MARK: – CustomPlayerView
// ─────────────────────────────────────────────
struct CustomPlayerView: View {
    // ─ المعاملات الواردة ─
    let itemId: String
    let itemTitle: String
    let itemImageUrl: String
    let videoUrl: String
    let videoUrl720: String
    let videoUrl1080: String
    let videoUrl360: String
    let subtitleUrl: String
    let subtitleVttUrl: String
    let episodeId: String
    let episodeTitle: String

    /// قائمة حلقات كاملة (اختيارية) للانتقال التلقائي
    var allEpisodes: [EpisodeItem] = []

    @Environment(\.presentationMode) var presentation
    @StateObject private var progressStore = WatchProgressStore.shared
    @StateObject private var settings      = AppSettings.shared

    // ─ Player State ─
    @State private var player: AVPlayer?
    @State private var isPlaying    = true
    @State private var currentTime: TimeInterval = 0
    @State private var duration: TimeInterval    = 1
    @State private var isDragging   = false
    @State private var seekTarget: TimeInterval  = 0
    @State private var timeObserver: Any?
    @State private var endObserver: Any?

    // ─ UI State ─
    @State private var showControls  = true
    @State private var hideTimer: Timer?
    @State private var isLocked      = false
    @State private var fitMode       = VideoFitMode.fit
    @State private var quality       = VideoQuality.auto
    @State private var isSpeedActive = false
    @State private var playbackSpeed = 1.0
    @State private var seekFeedback: (right: Bool, show: Bool) = (false, false)
    @State private var showEpisodes  = false
    @State private var currentEpId   = ""
    @State private var currentEpTitle = ""
    @State private var currentVideoUrl = ""
    @State private var currentVideoUrl360 = ""
    @State private var currentVideoUrl1080 = ""
    @State private var currentSubUrl = ""
    @State private var currentSubVtt = ""

    // ─ Subtitles ─
    @State private var cues: [SubtitleCue] = []
    @State private var activeSub = ""

    // ─ Misc ─
    @State private var saveTimer: Timer?
    @State private var errorMsg: String?

    // ─────────────────────────────────────────
    // MARK: – Font helper (✅ FIX الخطوط)
    // ─────────────────────────────────────────
    private func resolvedFont(size: CGFloat) -> Font {
        // الأسماء المتعددة التي قد يُسجّلها iOS لنفس الملف
        let candidates: [String]
        switch settings.subtitleFontName {
        case "Cairo", "Cairo-Regular":
            candidates = ["Cairo-Regular","Cairo","Cairo-Bold"]
        case "Rubik", "Rubik-Regular":
            candidates = ["Rubik-Regular","Rubik","Rubik-Bold"]
        case "Ibm", "IBMPlexArabic":
            candidates = ["IBMPlexArabic-Regular","IBMPlexArabic","IBMPlexArabic-Bold","Ibm"]
        default:
            candidates = [settings.subtitleFontName]
        }
        for name in candidates {
            if let uif = UIFont(name: name, size: size) { return Font(uif) }
        }
        return .system(size: size, weight: .bold, design: .rounded)
    }

    // ─────────────────────────────────────────
    // MARK: – Body
    // ─────────────────────────────────────────
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()

            if let p = player {
                VideoPlayerView(
                    player: p, gravity: fitMode.gravity,
                    onTap: {
                        if !isLocked {
                            withAnimation(.easeInOut(duration: 0.2)) { showControls.toggle() }
                            if showControls { scheduleHide() }
                        }
                    },
                    onLongPressBegan: {
                        guard !isLocked else { return }
                        isSpeedActive = true; p.rate = 2.0
                    },
                    onLongPressEnded: {
                        if isSpeedActive { isSpeedActive = false; p.rate = isPlaying ? Float(playbackSpeed) : 0 }
                    },
                    onDoubleTap: { isRight in
                        seekFeedback = (isRight, true)
                        DispatchQueue.main.asyncAfter(deadline: .now() + 0.55) { seekFeedback.show = false }
                        let delta: Double = isRight ? 10 : -10
                        let newT = max(0, min(duration, currentTime + delta))
                        p.seek(to: CMTime(seconds: newT, preferredTimescale: 600))
                        scheduleHide()
                    }
                )
                .ignoresSafeArea()

                // سرعة 2×
                if isSpeedActive {
                    VStack {
                        HStack(spacing: 6) {
                            Image(systemName: "forward.frame.fill")
                            Text("2× سرعة")
                        }
                        .font(.system(size: 14, weight: .bold))
                        .foregroundColor(.white)
                        .padding(.horizontal, 16).padding(.vertical, 8)
                        .background(.ultraThinMaterial, in: Capsule())
                        .padding(.top, 60)
                        Spacer()
                    }
                }

                // ترجمة
                if settings.subtitlesEnabled && !activeSub.isEmpty {
                    VStack {
                        Spacer()
                        Text(activeSub)
                            .font(resolvedFont(size: CGFloat(settings.subtitleFontSize)))
                            .foregroundColor(settings.subtitleColor)
                            .shadow(color: .black, radius: 3, x: 1, y: 1)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 20).padding(.vertical, 6)
                            .background(Color.black.opacity(settings.subtitleBgOpacity))
                            .cornerRadius(8)
                            .padding(.bottom, CGFloat(settings.subtitleBottomPad))
                    }
                    .allowsHitTesting(false)
                }

                // مؤشر التقديم/الترجيع
                if seekFeedback.show {
                    VStack {
                        Spacer()
                        SeekFeedbackView(isRight: seekFeedback.right).padding(.bottom, 130)
                    }
                    .transition(.opacity)
                    .animation(.easeOut(duration: 0.25), value: seekFeedback.show)
                }

                // أدوات التحكم
                if showControls || isLocked {
                    controlsOverlay(p: p)
                        .transition(.opacity)
                        .animation(.easeInOut(duration: 0.2), value: showControls)
                }

                // قائمة الحلقات (ترتفع بالإصبع)
                if showEpisodes {
                    VStack {
                        Spacer()
                        EpisodeListPanel(
                            episodes: allEpisodes,
                            currentEpisodeId: currentEpId,
                            onSelect: { ep in switchToEpisode(ep) },
                            isShown: $showEpisodes
                        )
                        .frame(height: UIScreen.main.bounds.height * 0.55)
                    }
                    .ignoresSafeArea(edges: .bottom)
                    .background(Color.black.opacity(0.4).ignoresSafeArea()
                                    .onTapGesture { withAnimation { showEpisodes = false } })
                    .transition(.opacity)
                    .animation(.spring(response: 0.4, dampingFraction: 0.85), value: showEpisodes)
                    .zIndex(10)
                }

            } else {
                // تحميل
                VStack(spacing: 16) {
                    ProgressView().tint(.white).scaleEffect(1.4)
                    Text("جاري التحميل...").foregroundColor(.white.opacity(0.8))
                    if let err = errorMsg { Text(err).foregroundColor(.red).font(.caption) }
                }
            }
        }
        .statusBar(hidden: true)
        .onAppear  { initPlayback() }
        .onDisappear { shutdown() }
    }

    // ─────────────────────────────────────────
    // MARK: – Controls Overlay
    // ─────────────────────────────────────────
    @ViewBuilder
    private func controlsOverlay(p: AVPlayer) -> some View {
        VStack {
            // ── شريط علوي ──
            HStack {
                if !isLocked {
                    Button { shutdown(); presentation.wrappedValue.dismiss() } label: {
                        Image(systemName: "chevron.left")
                            .font(.system(size: 18, weight: .bold))
                            .foregroundColor(.white)
                            .padding(12)
                            .background(.ultraThinMaterial, in: Circle())
                    }
                    Spacer()
                    VStack(alignment: .center, spacing: 2) {
                        Text(itemTitle)
                            .font(.system(size: 14, weight: .bold)).foregroundColor(.white).lineLimit(1)
                        if !currentEpTitle.isEmpty {
                            Text(currentEpTitle)
                                .font(.system(size: 11)).foregroundColor(.gray).lineLimit(1)
                        }
                    }
                    Spacer()
                    // زر قائمة الحلقات (للمسلسلات فقط)
                    if !allEpisodes.isEmpty {
                        Button { withAnimation { showEpisodes = true }; hideControls() } label: {
                            Image(systemName: "list.bullet")
                                .font(.system(size: 16, weight: .semibold))
                                .foregroundColor(.white)
                                .padding(12)
                                .background(.ultraThinMaterial, in: Circle())
                        }
                    }
                } else {
                    Spacer()
                }
                Button { withAnimation { isLocked.toggle() }; if isLocked { hideControls() } } label: {
                    Image(systemName: isLocked ? "lock.fill" : "lock.open")
                        .font(.system(size: 16, weight: .semibold))
                        .foregroundColor(.white)
                        .padding(12)
                        .background(.ultraThinMaterial, in: Circle())
                }
            }
            .padding(.horizontal, 16).padding(.top, 20)
            .background(LinearGradient(colors: [.black.opacity(0.75),.clear], startPoint: .top, endPoint: .bottom))

            Spacer()

            if !isLocked {
                // ── شريط سفلي ──
                VStack(spacing: 10) {
                    // شريط التقدم
                    HStack(spacing: 10) {
                        Text(formatTime(isDragging ? seekTarget : currentTime)).timeLabel()
                        Slider(
                            value: isDragging ? $seekTarget : $currentTime,
                            in: 0...max(duration, 1)
                        ) { editing in
                            isDragging = editing
                            if !editing {
                                p.seek(to: CMTime(seconds: seekTarget, preferredTimescale: 600))
                                currentTime = seekTarget
                                scheduleHide()
                            }
                        }
                        .accentColor(UT_RED)
                        Text(formatTime(duration)).timeLabel()
                    }
                    .padding(.horizontal, 16)

                    // أزرار التحكم المركزية
                    HStack(spacing: 44) {
                        // الحلقة السابقة
                        if !allEpisodes.isEmpty {
                            Button { skipEpisode(forward: false) } label: {
                                Image(systemName: "backward.end.fill")
                                    .font(.title2).foregroundColor(hasPrevEpisode ? .white : .gray)
                            }
                            .disabled(!hasPrevEpisode)
                        }

                        Button {
                            let t = max(0, currentTime - 10)
                            p.seek(to: CMTime(seconds: t, preferredTimescale: 600))
                            scheduleHide()
                        } label: {
                            Image(systemName: "gobackward.10").font(.title).foregroundColor(.white)
                        }

                        Button {
                            if isPlaying { p.pause() } else { p.rate = Float(playbackSpeed) }
                            isPlaying.toggle(); scheduleHide()
                        } label: {
                            Image(systemName: isPlaying ? "pause.circle.fill" : "play.circle.fill")
                                .font(.system(size: 68)).foregroundColor(UT_RED)
                        }

                        Button {
                            let t = min(duration, currentTime + 10)
                            p.seek(to: CMTime(seconds: t, preferredTimescale: 600))
                            scheduleHide()
                        } label: {
                            Image(systemName: "goforward.10").font(.title).foregroundColor(.white)
                        }

                        // الحلقة التالية
                        if !allEpisodes.isEmpty {
                            Button { skipEpisode(forward: true) } label: {
                                Image(systemName: "forward.end.fill")
                                    .font(.title2).foregroundColor(hasNextEpisode ? .white : .gray)
                            }
                            .disabled(!hasNextEpisode)
                        }
                    }

                    // جودة + نسبة عرض
                    HStack(spacing: 6) {
                        ForEach(VideoQuality.allCases) { q in
                            Button(q.rawValue) { switchQuality(to: q) }
                                .font(.system(size: 12, weight: quality == q ? .bold : .regular))
                                .foregroundColor(.white)
                                .padding(.horizontal, 10).padding(.vertical, 6)
                                .background(quality == q ? UT_RED : Color.white.opacity(0.12))
                                .cornerRadius(8)
                        }
                        Spacer()
                        Button {
                            let all = VideoFitMode.allCases
                            let i = all.firstIndex(of: fitMode) ?? 0
                            fitMode = all[(i+1) % all.count]
                        } label: {
                            HStack(spacing: 4) {
                                Image(systemName: "aspectratio")
                                Text(fitMode.rawValue)
                            }
                            .font(.system(size: 11)).foregroundColor(.white.opacity(0.75))
                        }
                    }
                    .padding(.horizontal, 16).padding(.bottom, 18)
                }
                .background(LinearGradient(colors: [.clear,.black.opacity(0.88)], startPoint: .top, endPoint: .bottom))
            }
        }
    }

    // ─────────────────────────────────────────
    // MARK: – Episode Navigation
    // ─────────────────────────────────────────
    private var currentEpIndex: Int? {
        allEpisodes.firstIndex(where: { $0.id == currentEpId })
    }
    private var hasNextEpisode: Bool {
        guard let i = currentEpIndex else { return false }
        return i + 1 < allEpisodes.count
    }
    private var hasPrevEpisode: Bool {
        guard let i = currentEpIndex else { return false }
        return i > 0
    }
    private func skipEpisode(forward: Bool) {
        guard let i = currentEpIndex else { return }
        let next = forward ? i + 1 : i - 1
        guard allEpisodes.indices.contains(next) else { return }
        switchToEpisode(allEpisodes[next])
    }
    private func switchToEpisode(_ ep: EpisodeItem) {
        saveCurrentProgress()
        currentEpId    = ep.id
        currentEpTitle = ep.title
        currentVideoUrl    = ep.url
        currentVideoUrl360 = ep.url360
        currentVideoUrl1080 = ep.url1080
        currentSubUrl  = ep.subtitleUrl
        currentSubVtt  = ep.subtitleVttUrl
        reloadPlayer(urlStr: resolvedUrl(quality: quality))
        loadSubtitles()
    }

    // ─────────────────────────────────────────
    // MARK: – Playback helpers
    // ─────────────────────────────────────────
    private func initPlayback() {
        currentEpId     = episodeId
        currentEpTitle  = episodeTitle
        currentVideoUrl     = videoUrl
        currentVideoUrl360  = videoUrl360
        currentVideoUrl1080 = videoUrl1080
        currentSubUrl   = subtitleUrl
        currentSubVtt   = subtitleVttUrl

        let resume = progressStore.progress(for: itemId)?.progressSeconds ?? 0
        reloadPlayer(urlStr: resolvedUrl(quality: quality), seekTo: resume > 5 ? resume : nil)
        loadSubtitles()
    }

    private func reloadPlayer(urlStr: String, seekTo: Double? = nil) {
        // إيقاف المراقبة القديمة
        if let obs = timeObserver { player?.removeTimeObserver(obs); timeObserver = nil }
        if let obs = endObserver  { NotificationCenter.default.removeObserver(obs); endObserver = nil }
        player?.pause(); player = nil
        cues = []; activeSub = ""; isPlaying = true; currentTime = 0; duration = 1

        guard !urlStr.isEmpty, let url = URL(string: urlStr) else {
            errorMsg = "رابط الفيديو غير صالح"; return
        }
        let item = AVPlayerItem(url: url)
        let p    = AVPlayer(playerItem: item)
        self.player = p

        if let t = seekTo { p.seek(to: CMTime(seconds: t, preferredTimescale: 600)) }
        p.play()

        // مدة الفيديو
        Task {
            if let dur = try? await item.asset.load(.duration), dur.isNumeric {
                DispatchQueue.main.async { self.duration = dur.seconds }
            }
        }

        // مراقبة الوقت
        timeObserver = p.addPeriodicTimeObserver(
            forInterval: CMTime(seconds: 0.25, preferredTimescale: 600), queue: .main
        ) { [weak p] t in
            guard let p = p else { return }
            if !self.isDragging { self.currentTime = t.seconds }
            // تحديث الترجمة
            if let cue = self.cues.first(where: { t.seconds >= $0.startTime && t.seconds <= $0.endTime }) {
                self.activeSub = cue.text
            } else { self.activeSub = "" }
            // تحديث حالة التشغيل
            self.isPlaying = p.rate > 0
        }

        // ✅ الدخول التلقائي للحلقة التالية (بدون weak لأن self هو View)
        endObserver = NotificationCenter.default.addObserver(
            forName: .AVPlayerItemDidPlayToEndTime, object: item, queue: .main
        ) { _ in
            self.isPlaying = false
            if self.hasNextEpisode { self.skipEpisode(forward: true) }
        }

        // حفظ دوري كل 5 ثوانٍ (بدون weak)
        saveTimer?.invalidate()
        saveTimer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            self.saveCurrentProgress()
        }

        scheduleHide()
    }

    private func loadSubtitles() {
        let url = currentSubVtt.isEmpty ? currentSubUrl : currentSubVtt
        guard !url.isEmpty else { return }
        SubtitleParser.parse(url: url) { self.cues = $0 }
    }

    private func saveCurrentProgress() {
        guard let p = player, duration > 0 else { return }
        progressStore.save(
            itemId: itemId, title: itemTitle, imageUrl: itemImageUrl,
            episodeId: currentEpId, episodeTitle: currentEpTitle,
            progress: p.currentTime().seconds, duration: duration,
            videoUrl: currentVideoUrl, videoUrl720: currentVideoUrl,
            videoUrl1080: currentVideoUrl1080, videoUrl360: currentVideoUrl360,
            subUrl: currentSubUrl, subVttUrl: currentSubVtt
        )
    }

    private func shutdown() {
        saveCurrentProgress()
        saveTimer?.invalidate(); hideTimer?.invalidate()
        if let obs = timeObserver { player?.removeTimeObserver(obs) }
        if let obs = endObserver  { NotificationCenter.default.removeObserver(obs) }
        player?.pause(); player = nil
    }

    private func scheduleHide() {
        hideTimer?.invalidate()
        hideTimer = Timer.scheduledTimer(withTimeInterval: 4, repeats: false) { _ in
            withAnimation { self.showControls = false }
        }
    }
    private func hideControls() { hideTimer?.invalidate(); withAnimation { showControls = false } }

    private func switchQuality(to q: VideoQuality) {
        guard let p = player else { return }
        let t = p.currentTime(); quality = q
        guard let url = URL(string: resolvedUrl(quality: q)) else { return }
        p.replaceCurrentItem(with: AVPlayerItem(url: url))
        p.seek(to: t); p.rate = isPlaying ? Float(playbackSpeed) : 0
    }

    private func resolvedUrl(quality: VideoQuality) -> String {
        func fix(_ u: String) -> String {
            if u.isEmpty { return "" }
            return u.hasPrefix("http") ? u : "https://movie.vodu.me/" + u
        }
        switch quality {
        case .q360:  return fix(currentVideoUrl360.isEmpty ? currentVideoUrl : currentVideoUrl360)
        case .q1080: return fix(currentVideoUrl1080.isEmpty ? currentVideoUrl : currentVideoUrl1080)
        default:     return fix(currentVideoUrl)
        }
    }

    private func formatTime(_ s: TimeInterval) -> String {
        guard s.isFinite else { return "00:00" }
        let h = Int(s)/3600, m = (Int(s)%3600)/60, sec = Int(s)%60
        return h > 0 ? String(format: "%02d:%02d:%02d", h, m, sec)
                     : String(format: "%02d:%02d", m, sec)
    }
}

// ─────────────────────────────────────────────
// MARK: – Utility View Extensions
// ─────────────────────────────────────────────
extension Text {
    func timeLabel() -> some View {
        self.font(.system(size: 12, weight: .semibold))
            .monospacedDigit().foregroundColor(.white)
    }
}
"""
with open("UTan/UTan/CustomPlayer.swift", "w", encoding="utf-8") as f:
    f.write(player_swift)
print("✅ CustomPlayer.swift كُتب")

# ─── 7. Views.swift (مع إضافة import UIKit) ───────────────────────────────────
views_swift = r"""import SwiftUI
import UIKit

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Loader
// ─────────────────────────────────────────────────────────────────────────────
struct UTanLoader: View {
    @Binding var isLoading: Bool
    @State private var pulse = false
    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            VStack(spacing: 24) {
                if let img = UIImage(named: "logo") {
                    Image(uiImage: img).resizable().scaledToFit()
                        .frame(width: 120, height: 120)
                        .scaleEffect(pulse ? 1.08 : 1.0)
                        .opacity(pulse ? 0.7 : 1.0)
                        .animation(.easeInOut(duration: 1.1).repeatForever(autoreverses: true), value: pulse)
                        .onAppear { pulse = true }
                } else {
                    Text("UTan")
                        .font(.system(size: 42, weight: .black, design: .rounded))
                        .foregroundColor(.white)
                }
                ProgressView().tint(UT_RED).scaleEffect(1.2)
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – PlayerData
// ─────────────────────────────────────────────────────────────────────────────
struct PlayerData: Identifiable {
    let id = UUID()
    let itemId: String
    let itemTitle: String
    let itemImageUrl: String
    let videoUrl: String
    let videoUrl720: String
    let videoUrl1080: String
    let videoUrl360: String
    let subtitleUrl: String
    let subtitleVttUrl: String
    let episodeId: String
    let episodeTitle: String
    var allEpisodes: [EpisodeItem] = []
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Poster Card
// ─────────────────────────────────────────────────────────────────────────────
struct PosterCard: View {
    let item: VideoItem
    var progress: WatchProgress? = nil
    private let W: CGFloat = 120
    private let H: CGFloat = 180

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            ZStack(alignment: .bottom) {
                AsyncImage(url: URL(string: item.imageUrl)) { img in
                    img.resizable().aspectRatio(contentMode: .fill)
                } placeholder: {
                    Color(white: 0.13)
                        .overlay(Image(systemName: "film").foregroundColor(.gray))
                }
                .frame(width: W, height: H).clipped().cornerRadius(14)

                LinearGradient(colors: [.clear, .black.opacity(0.75)],
                               startPoint: .center, endPoint: .bottom).cornerRadius(14)

                if let p = progress, p.durationSeconds > 0 {
                    VStack {
                        Spacer()
                        GeometryReader { geo in
                            ZStack(alignment: .leading) {
                                Color.white.opacity(0.3).frame(height: 3)
                                UT_RED.frame(
                                    width: geo.size.width * CGFloat(min(1, p.progressSeconds / p.durationSeconds)),
                                    height: 3)
                            }
                        }
                        .frame(height: 3).padding(.horizontal, 6).padding(.bottom, 6)
                    }
                }
            }
            .frame(width: W, height: H)
            .shadow(color: .black.opacity(0.45), radius: 6, x: 0, y: 4)

            Text(item.title)
                .font(.system(size: 11, weight: .semibold))
                .foregroundColor(.white.opacity(0.9))
                .lineLimit(2).frame(width: W, alignment: .leading)
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – MainTabView
// ─────────────────────────────────────────────────────────────────────────────
struct MainTabView: View {
    @StateObject private var scraper = MovieScraper()
    @State private var showLoader = true

    var body: some View {
        ZStack {
            if showLoader {
                UTanLoader(isLoading: $showLoader)
                    .onAppear {
                        DispatchQueue.main.asyncAfter(deadline: .now() + 2.5) { showLoader = false }
                    }
            } else {
                TabView {
                    HomeView(scraper: scraper)
                        .tabItem { Label("الرئيسية", systemImage: "house.fill") }
                    BrowseView(scraper: scraper)
                        .tabItem { Label("تصفح", systemImage: "square.grid.2x2.fill") }
                    SearchView(scraper: scraper)
                        .tabItem { Label("بحث", systemImage: "magnifyingglass") }
                    FavoritesView()
                        .tabItem { Label("قائمتي", systemImage: "heart.fill") }
                    SettingsView()
                        .tabItem { Label("المزيد", systemImage: "line.3.horizontal") }
                }
                .accentColor(UT_RED)
                .preferredColorScheme(.dark)
                .onAppear { configTabBar() }
            }
        }
    }
    private func configTabBar() {
        let a = UITabBarAppearance()
        a.configureWithOpaqueBackground()
        a.backgroundColor = UIColor(APP_BG)
        UITabBar.appearance().standardAppearance = a
        if #available(iOS 15.0, *) { UITabBar.appearance().scrollEdgeAppearance = a }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Network Cards Row
// ─────────────────────────────────────────────────────────────────────────────
private struct NetworkCard: Identifiable {
    let id = UUID()
    let assetName: String
    let categoryId: Int
}

private let networkCards: [NetworkCard] = [
    NetworkCard(assetName: "Netflix",  categoryId: 44),
    NetworkCard(assetName: "Anime",    categoryId: 2),
    NetworkCard(assetName: "Kids",     categoryId: 9018),
    NetworkCard(assetName: "Hbo",      categoryId: 73),
    NetworkCard(assetName: "Disney",   categoryId: 72),
    NetworkCard(assetName: "Marvel",   categoryId: 9014),
]

struct NetworkCardsRow: View {
    @ObservedObject var scraper: MovieScraper
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("تصفح حسب الشبكة")
                .font(.system(size: 20, weight: .bold)).foregroundColor(.white).padding(.horizontal, 20)
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 14) {
                    ForEach(networkCards) { card in
                        if let cat = SITE_CATEGORIES.first(where: { $0.id == card.categoryId }) {
                            NavigationLink(destination: CategoryListView(category: cat, scraper: scraper)) {
                                networkCardView(assetName: card.assetName)
                            }
                        }
                    }
                }
                .padding(.horizontal, 20)
            }
        }
    }

    @ViewBuilder
    private func networkCardView(assetName: String) -> some View {
        ZStack {
            if let img = UIImage(named: assetName) {
                Image(uiImage: img).resizable().aspectRatio(contentMode: .fill)
            } else {
                Color.white.opacity(0.08)
                Image(systemName: "play.tv.fill").font(.largeTitle).foregroundColor(UT_RED)
            }
        }
        .frame(width: 160, height: 100).clipped()
        .cornerRadius(16)
        .overlay(RoundedRectangle(cornerRadius: 16).stroke(UT_RED.opacity(0.3), lineWidth: 1))
        .shadow(color: .black.opacity(0.3), radius: 4, x: 0, y: 2)
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – HomeView
// ─────────────────────────────────────────────────────────────────────────────
struct HomeView: View {
    @ObservedObject var scraper: MovieScraper
    @ObservedObject private var progressStore = WatchProgressStore.shared
    @State private var playItem: PlayerData?

    var body: some View {
        NavigationView {
            ZStack(alignment: .top) {
                APP_BG.ignoresSafeArea()
                if scraper.isLoading {
                    UTanLoader(isLoading: .constant(true))
                } else {
                    ScrollView(showsIndicators: false) {
                        VStack(spacing: 0) {
                            if !scraper.heroItems.isEmpty {
                                HeroBanner(items: scraper.heroItems)
                                    .frame(height: UIScreen.main.bounds.height * 0.72)
                            }
                            VStack(alignment: .leading, spacing: 28) {
                                if !progressStore.recent.isEmpty {
                                    ContinueWatchingRow(items: progressStore.recent, playItem: $playItem)
                                        .padding(.top, -50).zIndex(1)
                                }
                                NetworkCardsRow(scraper: scraper)
                                ForEach(scraper.categories, id: \.name) { cat in
                                    if !cat.items.isEmpty { CategoryRow(title: cat.name, items: cat.items) }
                                }
                            }
                            .padding(.bottom, 110)
                        }
                    }
                    .ignoresSafeArea(.all, edges: .top)
                }

                // ✅ شعار ثابت (لا يتحرك)
                HStack {
                    if let img = UIImage(named: "logo") {
                        Image(uiImage: img).resizable().scaledToFit().frame(height: 54)
                    } else {
                        Text("UTan").font(.system(size: 28, weight: .black, design: .rounded)).foregroundColor(.white)
                    }
                    Spacer()
                }
                .padding(.horizontal, 20)
                .padding(.top, 52)
                .background(LinearGradient(colors: [APP_BG, APP_BG.opacity(0)], startPoint: .top, endPoint: .bottom))
            }
            .navigationBarHidden(true)
            .fullScreenCover(item: $playItem) { d in
                CustomPlayerView(
                    itemId: d.itemId, itemTitle: d.itemTitle, itemImageUrl: d.itemImageUrl,
                    videoUrl: d.videoUrl, videoUrl720: d.videoUrl720,
                    videoUrl1080: d.videoUrl1080, videoUrl360: d.videoUrl360,
                    subtitleUrl: d.subtitleUrl, subtitleVttUrl: d.subtitleVttUrl,
                    episodeId: d.episodeId, episodeTitle: d.episodeTitle,
                    allEpisodes: d.allEpisodes
                )
            }
        }
        .navigationViewStyle(StackNavigationViewStyle())
        .onAppear { if scraper.heroItems.isEmpty { scraper.fetchHome() } }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Hero Banner
// ─────────────────────────────────────────────────────────────────────────────
struct HeroBanner: View {
    let items: [VideoItem]
    @State private var current = 0
    @State private var timer: Timer?
    @ObservedObject private var fav = FavoritesStore.shared

    var body: some View {
        TabView(selection: $current) {
            ForEach(items.prefix(8).indices, id: \.self) { i in
                ZStack(alignment: .bottom) {
                    AsyncImage(url: URL(string: items[i].imageUrl)) { img in
                        img.resizable().aspectRatio(contentMode: .fill)
                    } placeholder: { Color(white: 0.06) }
                    .frame(maxWidth: .infinity, maxHeight: .infinity).clipped()

                    LinearGradient(colors: [.clear, APP_BG.opacity(0.6), APP_BG],
                                   startPoint: .center, endPoint: .bottom)

                    VStack(spacing: 14) {
                        Text(items[i].title)
                            .font(.system(size: 30, weight: .heavy))
                            .foregroundColor(.white)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 20)
                            .shadow(color: .black, radius: 4)

                        HStack(spacing: 20) {
                            NavigationLink(destination: DetailsView(itemId: items[i].id)) {
                                HStack { Image(systemName: "play.fill"); Text("شاهد الآن") }
                                    .font(.system(size: 16, weight: .bold))
                                    .padding(.horizontal, 28).padding(.vertical, 12)
                                    .background(UT_RED).foregroundColor(.white).cornerRadius(12)
                            }
                            Button { fav.toggle(item: items[i]) } label: {
                                VStack(spacing: 4) {
                                    Image(systemName: fav.isFavorite(items[i].id) ? "checkmark" : "plus")
                                        .font(.system(size: 20, weight: .bold))
                                    Text("قائمتي").font(.system(size: 10, weight: .semibold))
                                }.foregroundColor(.white)
                            }
                        }
                        .padding(.bottom, 90)
                    }
                }
                .tag(i)
            }
        }
        .tabViewStyle(.page(indexDisplayMode: .never))
        .onAppear  { timer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            withAnimation { current = (current+1) % min(items.count, 8) }
        }}
        .onDisappear { timer?.invalidate() }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Continue Watching Row
// ─────────────────────────────────────────────────────────────────────────────
struct ContinueWatchingRow: View {
    let items: [WatchProgress]
    @Binding var playItem: PlayerData?
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("متابعة المشاهدة")
                .font(.system(size: 20, weight: .bold)).foregroundColor(.white).padding(.horizontal, 20)
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 14) {
                    ForEach(items.prefix(10)) { p in
                        Button {
                            playItem = PlayerData(
                                itemId: p.itemId, itemTitle: p.title, itemImageUrl: p.imageUrl,
                                videoUrl: p.videoUrl, videoUrl720: p.videoUrl720,
                                videoUrl1080: p.videoUrl1080, videoUrl360: p.videoUrl360,
                                subtitleUrl: p.subtitleUrl, subtitleVttUrl: p.subtitleVttUrl,
                                episodeId: p.episodeId, episodeTitle: p.episodeTitle
                            )
                        } label: {
                            VStack(alignment: .leading, spacing: 6) {
                                ZStack(alignment: .center) {
                                    AsyncImage(url: URL(string: p.imageUrl)) { img in
                                        img.resizable().aspectRatio(contentMode: .fill)
                                    } placeholder: { Color(white: 0.12) }
                                    .frame(width: 158, height: 98).clipped().cornerRadius(12)
                                    Color.black.opacity(0.28).cornerRadius(12)
                                    Image(systemName: "play.circle.fill")
                                        .font(.system(size: 38)).foregroundColor(.white.opacity(0.9))
                                    if p.durationSeconds > 0 {
                                        VStack { Spacer()
                                            GeometryReader { geo in
                                                ZStack(alignment: .leading) {
                                                    Color.white.opacity(0.3).frame(height: 3)
                                                    UT_RED.frame(
                                                        width: geo.size.width * CGFloat(min(1, p.progressSeconds/p.durationSeconds)),
                                                        height: 3)
                                                }
                                            }
                                            .frame(height: 3).padding(.horizontal, 4).padding(.bottom, 4)
                                        }
                                    }
                                }.frame(width: 158, height: 98)
                                Text(p.title).font(.system(size: 13, weight: .bold)).foregroundColor(.white).lineLimit(1).frame(width: 158, alignment: .leading)
                                if !p.episodeTitle.isEmpty {
                                    Text(p.episodeTitle).font(.system(size: 11)).foregroundColor(.gray).lineLimit(1).frame(width: 158, alignment: .leading)
                                }
                            }
                        }
                    }
                }.padding(.horizontal, 20)
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Category Row
// ─────────────────────────────────────────────────────────────────────────────
struct CategoryRow: View {
    let title: String
    let items: [VideoItem]
    @ObservedObject private var store = WatchProgressStore.shared
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(title).font(.system(size: 20, weight: .bold)).foregroundColor(.white).padding(.horizontal, 20)
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 14) {
                    ForEach(items) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item, progress: store.progress(for: item.id))
                        }
                    }
                }.padding(.horizontal, 20)
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Browse View
// ─────────────────────────────────────────────────────────────────────────────
struct BrowseView: View {
    @ObservedObject var scraper: MovieScraper
    let cols = [GridItem(.flexible()), GridItem(.flexible())]
    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                ScrollView {
                    LazyVGrid(columns: cols, spacing: 16) {
                        ForEach(SITE_CATEGORIES) { cat in
                            NavigationLink(destination: CategoryListView(category: cat, scraper: scraper)) {
                                ZStack {
                                    RoundedRectangle(cornerRadius: 18)
                                        .fill(Color.white.opacity(0.07))
                                        .overlay(RoundedRectangle(cornerRadius: 18).stroke(UT_RED.opacity(0.25), lineWidth: 1))
                                    VStack(spacing: 10) {
                                        Image(systemName: "film.stack").font(.system(size: 30)).foregroundColor(UT_RED)
                                        Text(cat.nameAr).font(.system(size: 15, weight: .bold)).foregroundColor(.white)
                                        Text(cat.nameEn).font(.system(size: 10)).foregroundColor(.gray)
                                    }.padding(12)
                                }.frame(height: 105)
                            }
                        }
                    }.padding(16)
                }
            }
            .navigationTitle("تصفح")
        }.navigationViewStyle(StackNavigationViewStyle())
    }
}

struct CategoryListView: View {
    let category: SiteCategory
    @ObservedObject var scraper: MovieScraper
    @State private var items: [VideoItem] = []
    @State private var page = 1
    @State private var loading = false
    let cols = [GridItem(.adaptive(minimum: 110), spacing: 14)]
    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            ScrollView {
                LazyVGrid(columns: cols, spacing: 16) {
                    ForEach(items) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item)
                        }
                        .onAppear { if item.id == items.last?.id { loadMore() } }
                    }
                }.padding()
                if loading { ProgressView().tint(UT_RED).padding() }
            }
        }
        .navigationTitle(category.nameAr)
        .onAppear { if items.isEmpty { loadMore() } }
    }
    private func loadMore() {
        guard !loading else { return }
        loading = true
        scraper.fetchCategory(typeId: category.remoteId, page: page, useTag: category.isTag) { new, _ in
            items.append(contentsOf: new); page += 1; loading = false
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Search View
// ─────────────────────────────────────────────────────────────────────────────
struct SearchView: View {
    @ObservedObject var scraper: MovieScraper
    @State private var query = ""
    @State private var results: [VideoItem] = []
    @State private var isSearching = false
    let cols = [GridItem(.adaptive(minimum: 110), spacing: 14)]
    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                VStack(spacing: 0) {
                    HStack {
                        Image(systemName: "magnifyingglass").foregroundColor(.gray)
                        TextField("ابحث عن فيلم أو مسلسل...", text: $query)
                            .foregroundColor(.white)
                            .submitLabel(.search)
                            .onSubmit { doSearch() }
                        if !query.isEmpty {
                            Button { query = ""; results = [] } label: {
                                Image(systemName: "xmark.circle.fill").foregroundColor(.gray)
                            }
                        }
                    }
                    .padding(14)
                    .background(Color.white.opacity(0.1))
                    .cornerRadius(12)
                    .padding([.horizontal, .top], 16)

                    if isSearching {
                        ProgressView().tint(UT_RED).padding()
                    } else {
                        ScrollView {
                            LazyVGrid(columns: cols, spacing: 16) {
                                ForEach(results) { item in
                                    NavigationLink(destination: DetailsView(itemId: item.id)) { PosterCard(item: item) }
                                }
                            }.padding()
                        }
                    }
                }
            }
            .navigationTitle("البحث")
        }.navigationViewStyle(StackNavigationViewStyle())
    }
    private func doSearch() {
        guard !query.isEmpty else { return }
        isSearching = true
        scraper.search(query: query) { r in results = r; isSearching = false }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Favorites View
// ─────────────────────────────────────────────────────────────────────────────
struct FavoritesView: View {
    @ObservedObject private var fav = FavoritesStore.shared
    let cols = [GridItem(.adaptive(minimum: 110), spacing: 14)]
    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                if fav.items.isEmpty {
                    VStack(spacing: 20) {
                        Image(systemName: "heart.slash").font(.system(size: 60)).foregroundColor(.gray)
                        Text("قائمتك فارغة").foregroundColor(.gray)
                    }
                } else {
                    ScrollView {
                        LazyVGrid(columns: cols, spacing: 16) {
                            ForEach(fav.items) { item in
                                NavigationLink(destination: DetailsView(itemId: item.id)) { PosterCard(item: item) }
                            }
                        }.padding()
                    }
                }
            }
            .navigationTitle("قائمتي")
        }.navigationViewStyle(StackNavigationViewStyle())
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Settings View
// ─────────────────────────────────────────────────────────────────────────────
struct SettingsView: View {
    @ObservedObject var settings = AppSettings.shared
    @ObservedObject var history  = WatchProgressStore.shared
    @State private var cleared = false

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                Form {
                    // ── الترجمة ──
                    Section(header: Text("إعدادات الترجمة").foregroundColor(UT_RED)) {
                        Toggle("تفعيل الترجمة", isOn: $settings.subtitlesEnabled)
                        if settings.subtitlesEnabled {
                            // اختيار الخط
                            VStack(alignment: .leading, spacing: 8) {
                                Text("الخط").font(.caption).foregroundColor(.gray)
                                // ✅ FIX: نستخدم الاسم الفعلي المُسجّل في iOS
                                Picker("", selection: $settings.subtitleFontName) {
                                    Text("Cairo").tag("Cairo-Regular")
                                    Text("Rubik").tag("Rubik-Regular")
                                    Text("IBM Plex").tag("IBMPlexArabic-Regular")
                                }
                                .pickerStyle(.segmented)
                            }
                            VStack(alignment: .leading, spacing: 4) {
                                Text("حجم الخط: \(Int(settings.subtitleFontSize))").font(.callout)
                                Slider(value: $settings.subtitleFontSize, in: 14...40, step: 1).accentColor(UT_RED)
                            }
                            VStack(alignment: .leading, spacing: 4) {
                                Text("الهامش السفلي: \(Int(settings.subtitleBottomPad))").font(.callout)
                                Slider(value: $settings.subtitleBottomPad, in: 20...180, step: 5).accentColor(UT_RED)
                            }
                            VStack(alignment: .leading, spacing: 4) {
                                Text("شفافية الخلفية: \(Int(settings.subtitleBgOpacity*100))%").font(.callout)
                                Slider(value: $settings.subtitleBgOpacity, in: 0...1, step: 0.1).accentColor(UT_RED)
                            }
                            HStack(spacing: 12) {
                                ForEach(["#FFFFFF","#FFFF00","#00FFFF","#FF8C00"], id: \.self) { hex in
                                    Circle().fill(Color(hex: hex)).frame(width: 32, height: 32)
                                        .overlay(Circle().stroke(Color.white, lineWidth: settings.subtitleColorHex == hex ? 3 : 0))
                                        .onTapGesture { settings.subtitleColorHex = hex }
                                }
                            }
                            // معاينة
                            Text("هذه معاينة الترجمة")
                                .font(.system(size: CGFloat(settings.subtitleFontSize) * 0.6))
                                .foregroundColor(settings.subtitleColor)
                                .padding(6).background(Color.black.opacity(settings.subtitleBgOpacity)).cornerRadius(6)
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    // ── البيانات ──
                    Section(header: Text("البيانات والتخزين").foregroundColor(UT_RED)) {
                        NavigationLink(destination: HistoryView()) {
                            Label("سجل المشاهدة (\(history.recent.count))", systemImage: "clock")
                        }
                        Button(role: .destructive) {
                            settings.clearCache(); cleared = true
                            DispatchQueue.main.asyncAfter(deadline: .now() + 2) { cleared = false }
                        } label: {
                            Label(cleared ? "تم المسح!" : "مسح التخزين المؤقت والسجل",
                                  systemImage: cleared ? "checkmark.circle" : "trash")
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    // ── معلومات ──
                    Section(header: Text("عن التطبيق").foregroundColor(UT_RED)) {
                        HStack {
                            Text("الإصدار")
                            Spacer()
                            Text("5.0").foregroundColor(.gray)
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)
                }
                .scrollContentBackground(.hidden)
            }
            .navigationTitle("المزيد")
        }.navigationViewStyle(StackNavigationViewStyle())
    }
}

struct HistoryView: View {
    @ObservedObject var store = WatchProgressStore.shared
    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            List {
                ForEach(store.recent) { p in
                    HStack(spacing: 12) {
                        AsyncImage(url: URL(string: p.imageUrl)) { img in
                            img.resizable().aspectRatio(contentMode: .fill)
                        } placeholder: { Color.gray }
                        .frame(width: 50, height: 75).cornerRadius(8)
                        VStack(alignment: .leading, spacing: 4) {
                            Text(p.title).font(.headline).foregroundColor(.white)
                            if !p.episodeTitle.isEmpty { Text(p.episodeTitle).font(.caption).foregroundColor(.gray) }
                            if p.durationSeconds > 0 {
                                ProgressView(value: min(1, p.progressSeconds/p.durationSeconds)).tint(UT_RED)
                            }
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                }
                .onDelete { idx in idx.forEach { i in store.remove(itemId: store.recent[i].itemId) } }
            }
            .scrollContentBackground(.hidden)
        }
        .navigationTitle("سجل المشاهدة")
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Details View
// ─────────────────────────────────────────────────────────────────────────────
struct DetailsView: View {
    let itemId: String
    @StateObject private var scraper     = MovieScraper()
    @ObservedObject private var fav      = FavoritesStore.shared
    @ObservedObject private var progress = WatchProgressStore.shared

    @State private var details: MediaDetails?
    @State private var loading        = true
    @State private var playerData: PlayerData?
    @State private var selectedSeason = ""

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            if loading {
                UTanLoader(isLoading: $loading)
            } else if let d = details {
                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 0) {
                        // ── صورة + overlay ──
                        ZStack(alignment: .bottomLeading) {
                            AsyncImage(url: URL(string: d.imageUrl)) { img in
                                img.resizable().aspectRatio(contentMode: .fill)
                            } placeholder: { Color(white: 0.08) }
                            .frame(maxWidth: .infinity).frame(height: 340).clipped()

                            LinearGradient(colors: [.clear, APP_BG.opacity(0.7), APP_BG],
                                           startPoint: .top, endPoint: .bottom)

                            VStack(alignment: .leading, spacing: 12) {
                                Text(d.title)
                                    .font(.system(size: 26, weight: .heavy)).foregroundColor(.white)

                                // badges
                                HStack(spacing: 8) {
                                    if !d.year.isEmpty    { badge(d.year) }
                                    if !d.rating.isEmpty  {
                                        HStack(spacing: 3) {
                                            Image(systemName: "star.fill").foregroundColor(.yellow)
                                            Text(d.rating)
                                        }.font(.system(size: 12, weight: .bold)).foregroundColor(.white)
                                    }
                                    if !d.runtime.isEmpty { badge(d.runtime) }
                                }

                                // أزرار
                                HStack(spacing: 14) {
                                    if d.isMovie {
                                        Button { playMovie(d: d) } label: {
                                            HStack { Image(systemName: "play.fill"); Text("شاهد الآن") }
                                                .font(.system(size: 16, weight: .bold))
                                                .frame(maxWidth: .infinity)
                                                .padding(12).background(UT_RED).foregroundColor(.white).cornerRadius(12)
                                        }
                                    }
                                    Button {
                                        fav.toggle(item: VideoItem(id: itemId, title: d.title, imageUrl: d.imageUrl, type: "post"))
                                    } label: {
                                        Image(systemName: fav.isFavorite(itemId) ? "heart.fill" : "heart")
                                            .font(.title2).foregroundColor(fav.isFavorite(itemId) ? UT_RED : .white)
                                            .padding(12).background(Color.white.opacity(0.12)).cornerRadius(12)
                                    }
                                }
                                .padding(.top, 8)
                            }
                            .padding(.horizontal, 18).padding(.bottom, 18)
                        }

                        // ── ملخص ──
                        if !d.synopsis.isEmpty {
                            VStack(alignment: .leading, spacing: 6) {
                                Text("القصة").font(.system(size: 17, weight: .bold)).foregroundColor(.white)
                                Text(d.synopsis).font(.system(size: 14)).foregroundColor(.gray).lineSpacing(5)
                            }.padding(18)
                        }

                        // ── معلومات ──
                        if !d.genre.isEmpty {
                            HStack { Text("النوع:").bold().foregroundColor(.white); Text(d.genre).foregroundColor(.gray) }
                                .font(.system(size: 13)).padding(.horizontal, 18).padding(.bottom, 6)
                        }

                        // ── حلقات ──
                        if !d.isMovie && !d.sortedSeasons.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                // أزرار الموسم
                                ScrollView(.horizontal, showsIndicators: false) {
                                    HStack(spacing: 10) {
                                        ForEach(d.sortedSeasons, id: \.self) { s in
                                            Button { selectedSeason = s } label: {
                                                Text(s).font(.system(size: 15, weight: .bold))
                                                    .padding(.horizontal, 18).padding(.vertical, 9)
                                                    .background(selectedSeason == s ? UT_RED : Color.white.opacity(0.08))
                                                    .foregroundColor(.white).cornerRadius(10)
                                            }
                                        }
                                    }.padding(.horizontal, 18)
                                }

                                // قائمة الحلقات
                                LazyVStack(spacing: 10) {
                                    let eps = d.seasonsDict[selectedSeason] ?? []
                                    ForEach(eps) { ep in
                                        episodeRow(ep: ep, d: d)
                                    }
                                }
                            }
                            .padding(.bottom, 50)
                        }
                    }
                }
            }
        }
        .navigationBarTitleDisplayMode(.inline)
        .fullScreenCover(item: $playerData) { data in
            CustomPlayerView(
                itemId: data.itemId, itemTitle: data.itemTitle, itemImageUrl: data.itemImageUrl,
                videoUrl: data.videoUrl, videoUrl720: data.videoUrl720,
                videoUrl1080: data.videoUrl1080, videoUrl360: data.videoUrl360,
                subtitleUrl: data.subtitleUrl, subtitleVttUrl: data.subtitleVttUrl,
                episodeId: data.episodeId, episodeTitle: data.episodeTitle,
                allEpisodes: data.allEpisodes
            )
        }
        .onAppear {
            scraper.fetchDetails(id: itemId) { d in
                details = d
                selectedSeason = d.sortedSeasons.first ?? ""
                loading = false
            }
        }
    }

    @ViewBuilder
    private func episodeRow(ep: EpisodeItem, d: MediaDetails) -> some View {
        let prog = progress.progress(for: itemId)
        let isWatched = prog?.episodeId == ep.id
        HStack(spacing: 12) {
            Button {
                playerData = PlayerData(
                    itemId: itemId, itemTitle: d.title, itemImageUrl: d.imageUrl,
                    videoUrl: ep.url, videoUrl720: ep.url720,
                    videoUrl1080: ep.url1080, videoUrl360: ep.url360,
                    subtitleUrl: ep.subtitleUrl, subtitleVttUrl: ep.subtitleVttUrl,
                    episodeId: ep.id, episodeTitle: ep.title,
                    allEpisodes: d.episodes           // ✅ نمرر كل الحلقات للانتقال التلقائي
                )
            } label: {
                HStack(spacing: 12) {
                    ZStack {
                        Circle().fill(isWatched ? UT_RED : Color.white.opacity(0.08)).frame(width: 38, height: 38)
                        Image(systemName: "play.fill").font(.system(size: 14)).foregroundColor(.white)
                    }
                    VStack(alignment: .leading, spacing: 3) {
                        Text(ep.title).font(.system(size: 13, weight: .semibold))
                            .foregroundColor(isWatched ? UT_RED : .white).lineLimit(2)
                        if isWatched, let p = prog, p.durationSeconds > 0 {
                            ProgressView(value: min(1, p.progressSeconds / p.durationSeconds))
                                .tint(UT_RED).frame(maxWidth: .infinity)
                        }
                    }
                    Spacer()
                }
                .padding(12)
                .background(Color.white.opacity(isWatched ? 0.08 : 0.04))
                .cornerRadius(12)
            }
            .buttonStyle(PlainButtonStyle())

            // زر التحميل
            Button {
                DownloadManager.shared.startDownload(
                    item: VideoItem(id: ep.id, title: ep.title, imageUrl: d.imageUrl, type: "post"),
                    isMovie: false, vUrl: ep.url, sUrl: ep.subtitleUrl)
            } label: {
                Image(systemName: "arrow.down.circle").font(.title3).foregroundColor(.gray)
            }
        }
        .padding(.horizontal, 18)
    }

    private func playMovie(d: MediaDetails) {
        playerData = PlayerData(
            itemId: itemId, itemTitle: d.title, itemImageUrl: d.imageUrl,
            videoUrl: d.movieUrl, videoUrl720: d.movieUrl720,
            videoUrl1080: d.movieUrl1080, videoUrl360: d.movieUrl360,
            subtitleUrl: d.movieSubtitleUrl, subtitleVttUrl: d.movieSubtitleVttUrl,
            episodeId: "", episodeTitle: ""
        )
    }

    private func badge(_ text: String) -> some View {
        Text(text).font(.system(size: 11, weight: .bold))
            .padding(.horizontal, 8).padding(.vertical, 3)
            .background(Color.white.opacity(0.13)).cornerRadius(5).foregroundColor(.white)
    }
}
"""
with open("UTan/UTan/Views.swift", "w", encoding="utf-8") as f:
    f.write(views_swift)
print("✅ Views.swift كُتب")

print()
print("╔══════════════════════════════════════════════╗")
print("║  ✅  UTan v5.0 – كل الإصلاحات مطبّقة       ║")
print("╠══════════════════════════════════════════════╣")
print("║  🔤 الخطوط: Info.plist يسجّل الملفات صراحةً ║")
print("║     UTanApp يطبع الأسماء عند التشغيل        ║")
print("║     SettingsView يستخدم الأسماء الفعلية      ║")
print("║  📐 الكاردات: أبعاد ثابتة 120×180            ║")
print("║  🖼  الشعار: ثابت لا يتحرك (overlay فوق)     ║")
print("║  🔍 السكرابينج: regex مُصحَّح لهيكل الموقع  ║")
print("║  📺 قائمة حلقات: ترتفع بالإصبع داخل المشغل  ║")
print("║  ⏭  انتقال تلقائي للحلقة التالية عند الانتهاء║")
print("║  ⏩ أزرار حلقة سابقة/تالية في المشغل        ║")
print("║  👆 double tap: تقديم/ترجيع بدون تداخل      ║")
print("║  🚫 إزالة البلور من زر التشغيل               ║")
print("║  💾 pbxproj يُضمّن ملفات الخطوط الستة        ║")
print("║  🔧 تم إصلاح خطأ [weak self] في CustomPlayer║")
print("║  📦 إضافة import UIKit للأماكن المطلوبة      ║")
print("╚══════════════════════════════════════════════╝")