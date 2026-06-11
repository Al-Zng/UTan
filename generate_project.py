import os

# إنشاء هيكل المجلدات
os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# 1. كتابة ملف project.pbxproj (نفس المحتوى السابق مع تحديث مراجع الخطوط إذا لزم الأمر)
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
\t\t010101012C12345600000028 /* Cairo-Bold-1.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000029 /* Cairo-Bold-1.ttf */; };
\t\t010101012C1234560000002A /* Rubik-Bold.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000002B /* Rubik-Bold.ttf */; };
\t\t010101012C1234560000002C /* IBMPlexArabic-Bold.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000002D /* IBMPlexArabic-Bold.ttf */; };
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
\t\t010101012C12345600000029 /* Cairo-Bold-1.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "Cairo-Bold-1.ttf"; sourceTree = "<group>"; };
\t\t010101012C1234560000002B /* Rubik-Bold.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "Rubik-Bold.ttf"; sourceTree = "<group>"; };
\t\t010101012C1234560000002D /* IBMPlexArabic-Bold.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "IBMPlexArabic-Bold.ttf"; sourceTree = "<group>"; };
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
\t\t\t\t010101012C12345600000029 /* Cairo-Bold-1.ttf */,
\t\t\t\t010101012C1234560000002B /* Rubik-Bold.ttf */,
\t\t\t\t010101012C1234560000002D /* IBMPlexArabic-Bold.ttf */,
\t\t\t);
\t\t\tpath = UTan;
\t\t\tsourceTree = "<group>";
\t\t};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
\t\t010101012C12345600000010 /* UTan */ = {
\t\t\tisa = PBXNativeTarget;
\t\t\tbuildConfigurationList = 010101012C12345600000011 /* Build configuration list for PBXNativeTarget "UTan" */;
\t\t\tbuildPhases = (
\t\t\t\t010101012C12345600000012 /* Sources */,
\t\t\t\t010101012C1234560000000D /* Frameworks */,
\t\t\t\t010101012C12345600000028 /* Resources */,
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
\t\t\tbuildConfigurationList = 010101012C12345600000014 /* Build configuration list for PBXProject "UTan" */;
\t\t\tcompatibilityVersion = "Xcode 14.0";
\t\t\tdevelopmentRegion = en;
\t\t\thasScannedForEncodings = 0;
\t\t\tknownRegions = (
\t\t\t\ten,
\t\t\t\tBase,
\t\t\t\tar,
\t\t\t);
\t\t\tmainGroup = 010101012C1234560000000E /* MainGroup */;
\t\t\tproductRefGroup = 010101012C1234560000000E /* MainGroup */;
\t\t\tprojectDirPath = "";
\t\t\tprojectRoot = "";
\t\t\ttargets = (
\t\t\t\t010101012C12345600000010 /* UTan */,
\t\t\t);
\t\t};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
\t\t010101012C12345600000028 /* Resources */ = {
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
\t\t\t\t010101012C12345600000028 /* Cairo-Bold-1.ttf in Resources */,
\t\t\t\t010101012C1234560000002A /* Rubik-Bold.ttf in Resources */,
\t\t\t\t010101012C1234560000002C /* IBMPlexArabic-Bold.ttf in Resources */,
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
\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = (
\t\t\t\t\t"DEBUG=1",
\t\t\t\t\t"$(inherited)",
\t\t\t\t);
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
\t\t010101012C12345600000017 /* Debug */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCODE_SIGNING_ALLOWED = NO;
\t\t\t\tCODE_SIGNING_REQUIRED = NO;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_ASSET_PATHS = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tINFOPLIST_FILE = UTan/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 16.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t};
\t\t\tname = Debug;
\t\t};
\t\t010101012C12345600000018 /* Release */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCODE_SIGNING_ALLOWED = NO;
\t\t\t\tCODE_SIGNING_REQUIRED = NO;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_ASSET_PATHS = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tINFOPLIST_FILE = UTan/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 16.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
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
\t\t010101012C12345600000011 /* Build configuration list for PBXNativeTarget "UTan" */ = {
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t010101012C12345600000017 /* Debug */,
\t\t\t\t010101012C12345600000018 /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t};
\t\t010101012C12345600000014 /* Build configuration list for PBXProject "UTan" */ = {
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

# 2. كتابة Info.plist (مع إضافة أسماء خطوط TrueType الصحيحة)
info_plist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>en</string>
    <key>CFBundleExecutable</key>
    <string>$(EXECUTABLE_NAME)</string>
    <key>CFBundleIdentifier</key>
    <string>com.mustaqil.utan</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleName</key>
    <string>UTan</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>4.0</string>
    <key>CFBundleVersion</key>
    <string>4</string>
    <key>LSRequiresIPhoneOS</key>
    <true/>
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <true/>
    </dict>
    <key>UIBackgroundModes</key>
    <array>
        <string>fetch</string>
        <string>processing</string>
    </array>
    <key>UILaunchScreen</key>
    <dict/>
    <key>UISupportedInterfaceOrientations</key>
    <array>
        <string>UIInterfaceOrientationPortrait</string>
        <string>UIInterfaceOrientationLandscapeLeft</string>
        <string>UIInterfaceOrientationLandscapeRight</string>
    </array>
    <key>UIUserInterfaceStyle</key>
    <string>Dark</string>
    <key>UIAppFonts</key>
    <array>
        <string>Cairo-Bold-1.ttf</string>
        <string>Rubik-Bold.ttf</string>
        <string>IBMPlexArabic-Bold.ttf</string>
    </array>
</dict>
</plist>
"""

with open("UTan/UTan/Info.plist", "w", encoding="utf-8") as f:
    f.write(info_plist)

# 3. كتابة UTanApp.swift (نفس السابق)
app_swift = """import SwiftUI

@main
struct UTanApp: App {
    var body: some Scene {
        WindowGroup {
            MainTabView()
        }
    }
}
"""

with open("UTan/UTan/UTanApp.swift", "w", encoding="utf-8") as f:
    f.write(app_swift)

# 4. كتابة Scraper.swift (مع تحسين جودة الصورة وإصلاح تحميل الأقسام)
scraper_swift = r"""import Foundation
import SwiftUI

// ─────────────────────────────────────────────
// MARK: – Global Colors & Configs
// ─────────────────────────────────────────────

let APP_BG     = Color(red: 0.05, green: 0.02, blue: 0.09)
let UT_RED     = Color(red: 0.89, green: 0.04, blue: 0.08)
let UT_WHITE   = Color.white
let UT_SURFACE = Color.white.opacity(0.12)

class AppSettings: ObservableObject {
    static let shared = AppSettings()

    @AppStorage("sub_fontSize")   var subtitleFontSize: Double  = 22.0
    @AppStorage("sub_colorHex")   var subtitleColorHex: String  = "#FFFFFF"
    @AppStorage("sub_bgOpacity")  var subtitleBgOpacity: Double = 0.6
    @AppStorage("sub_bottomPad")  var subtitleBottomPad: Double = 60.0
    @AppStorage("sub_enabled")    var subtitlesEnabled: Bool    = true
    @AppStorage("sub_fontName")   var subtitleFontName: String  = "Cairo"

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
    let url720: String
    let url1080: String
    let url360: String
    let subtitleUrl: String
    let subtitleVttUrl: String

    var season: String {
        let pattern = "(?i)(S\\d+|موسم \\d+)"
        if let rx = try? NSRegularExpression(pattern: pattern),
           let match = rx.firstMatch(in: title, range: NSRange(location: 0, length: title.count)) {
            let nsString = title as NSString
            return nsString.substring(with: match.range)
                .replacingOccurrences(of: "s", with: "S")
                .replacingOccurrences(of: "S", with: "الموسم ")
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

    var seasonsDict: [String: [EpisodeItem]] {
        Dictionary(grouping: episodes, by: { $0.season })
    }
    var sortedSeasons: [String] {
        seasonsDict.keys.sorted { s1, s2 in
            let n1 = Int(s1.components(separatedBy: CharacterSet.decimalDigits.inverted).joined()) ?? 0
            let n2 = Int(s2.components(separatedBy: CharacterSet.decimalDigits.inverted).joined()) ?? 0
            return n1 < n2
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Watch Progress & Favorites
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
    private let key = "UTanWatchProgress_v3"

    @Published var allProgress: [String: WatchProgress] = [:]

    private init() { load() }

    func save(itemId: String, title: String, imageUrl: String,
              episodeId: String, episodeTitle: String,
              progress: Double, duration: Double,
              videoUrl: String, videoUrl720: String, videoUrl1080: String, videoUrl360: String,
              subUrl: String, subVttUrl: String) {
        let record = WatchProgress(
            itemId: itemId, title: title, imageUrl: imageUrl,
            episodeId: episodeId, episodeTitle: episodeTitle,
            progressSeconds: progress, durationSeconds: duration,
            updatedAt: Date(),
            videoUrl: videoUrl, videoUrl720: videoUrl720, videoUrl1080: videoUrl1080, videoUrl360: videoUrl360,
            subtitleUrl: subUrl, subtitleVttUrl: subVttUrl
        )
        allProgress[itemId] = record
        persist()
    }

    func remove(itemId: String) {
        allProgress.removeValue(forKey: itemId)
        persist()
    }

    func clearAll() {
        allProgress.removeAll()
        persist()
    }

    func progress(for itemId: String) -> WatchProgress? { allProgress[itemId] }

    var recent: [WatchProgress] {
        allProgress.values.sorted { $0.updatedAt > $1.updatedAt }
    }

    private func load() {
        guard let data = UserDefaults.standard.data(forKey: key),
              let decoded = try? JSONDecoder().decode([String: WatchProgress].self, from: data)
        else { return }
        allProgress = decoded
    }

    private func persist() {
        if let data = try? JSONEncoder().encode(allProgress) {
            UserDefaults.standard.set(data, forKey: key)
        }
    }
}

class FavoritesStore: ObservableObject {
    static let shared = FavoritesStore()
    private let key = "UTanFavorites_v1"

    @Published var items: [VideoItem] = []

    private init() { load() }

    func toggle(item: VideoItem) {
        if let idx = items.firstIndex(where: { $0.id == item.id }) {
            items.remove(at: idx)
        } else {
            items.insert(item, at: 0)
        }
        persist()
    }

    func isFavorite(_ id: String) -> Bool {
        items.contains(where: { $0.id == id })
    }

    private func load() {
        if let data = UserDefaults.standard.data(forKey: key),
           let decoded = try? JSONDecoder().decode([VideoItem].self, from: data) {
            items = decoded
        }
    }
    private func persist() {
        if let data = try? JSONEncoder().encode(items) {
            UserDefaults.standard.set(data, forKey: key)
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Background Downloads Manager
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
    var localSubPath: String?
}

class DownloadManager: NSObject, ObservableObject, URLSessionDownloadDelegate {
    static let shared = DownloadManager()
    private let key = "UTanDownloads_v1"

    @Published var activeDownloads: [DownloadTaskItem] = []
    private var session: URLSession!
    private var taskMap: [Int: String] = [:]

    private override init() {
        super.init()
        let config = URLSessionConfiguration.background(withIdentifier: "com.mustaqil.utan.background")
        session = URLSession(configuration: config, delegate: self, delegateQueue: nil)
        load()
    }

    func startDownload(item: VideoItem, isMovie: Bool, vUrl: String, sUrl: String) {
        guard !activeDownloads.contains(where: { $0.id == item.id }) else { return }
        let dl = DownloadTaskItem(id: item.id, title: item.title, imageUrl: item.imageUrl,
                                  isMovie: isMovie, videoUrl: vUrl, subtitleUrl: sUrl)
        DispatchQueue.main.async {
            self.activeDownloads.append(dl)
            self.persist()
        }
        if let url = URL(string: vUrl) {
            let task = session.downloadTask(with: url)
            taskMap[task.taskIdentifier] = item.id
            task.resume()
        }
    }

    func cancel(id: String) {
        DispatchQueue.main.async {
            self.activeDownloads.removeAll(where: { $0.id == id })
            self.persist()
        }
    }

    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didWriteData bytesWritten: Int64, totalBytesWritten: Int64,
                    totalBytesExpectedToWrite: Int64) {
        guard let id = taskMap[downloadTask.taskIdentifier], totalBytesExpectedToWrite > 0 else { return }
        let progress = Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
        DispatchQueue.main.async {
            if let idx = self.activeDownloads.firstIndex(where: { $0.id == id }) {
                self.activeDownloads[idx].progress = progress
            }
        }
    }

    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didFinishDownloadingTo location: URL) {
        guard let id = taskMap[downloadTask.taskIdentifier] else { return }
        let dest = FileManager.default.temporaryDirectory.appendingPathComponent(id + ".mp4")
        try? FileManager.default.removeItem(at: dest)
        try? FileManager.default.moveItem(at: location, to: dest)
        DispatchQueue.main.async {
            if let idx = self.activeDownloads.firstIndex(where: { $0.id == id }) {
                self.activeDownloads[idx].isCompleted = true
                self.activeDownloads[idx].localVideoPath = dest.path
                self.persist()
                UISaveVideoAtPathToSavedPhotosAlbum(dest.path, nil, nil, nil)
            }
        }
    }

    private func load() {
        if let data = UserDefaults.standard.data(forKey: key),
           let d = try? JSONDecoder().decode([DownloadTaskItem].self, from: data) {
            activeDownloads = d
        }
    }
    private func persist() {
        if let data = try? JSONEncoder().encode(activeDownloads) {
            UserDefaults.standard.set(data, forKey: key)
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Site categories map
// ─────────────────────────────────────────────

struct SiteCategory: Identifiable {
    let id: Int
    let remoteId: Int
    let isTag: Bool
    let nameAr: String
    let nameEn: String

    init(id: Int, remoteId: Int? = nil, isTag: Bool = false, nameAr: String, nameEn: String) {
        self.id = id
        self.remoteId = remoteId ?? id
        self.isTag = isTag
        self.nameAr = nameAr
        self.nameEn = nameEn
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
    SiteCategory(id: 44, remoteId: 44, isTag: true, nameAr: "نيتفلكس",  nameEn: "Netflix"),
    SiteCategory(id: 9014, remoteId: 14, isTag: true, nameAr: "عالم مارفل",  nameEn: "Marvel"),
    SiteCategory(id: 73, remoteId: 73, isTag: true, nameAr: "اتش بي او ماكس",  nameEn: "HBO Max"),
    SiteCategory(id: 72, remoteId: 72, isTag: true, nameAr: "ديزني",  nameEn: "Disney+"),
    SiteCategory(id: 9018, remoteId: 18, isTag: true, nameAr: "للاطفال",  nameEn: "For KIDS")
]

// ─────────────────────────────────────────────
// MARK: – Helper: تحسين جودة الصورة
// ─────────────────────────────────────────────
func optimizeImageUrl(_ url: String, width: Int = 400, height: Int = 600) -> String {
    if url.contains("w=750") || url.contains("h=388") {
        return url
    }
    let separator = url.contains("?") ? "&" : "?"
    return "\(url)\(separator)w=\(width)&h=\(height)&crop-to-fit"
}

// ─────────────────────────────────────────────
// MARK: – Main scraper / network layer
// ─────────────────────────────────────────────

class MovieScraper: ObservableObject {
    @Published var heroItems: [VideoItem] = []
    @Published var categories: [(name: String, items: [VideoItem])] = []
    @Published var allItemsPool: [VideoItem] = []
    @Published var isLoading = false

    let baseUrl = "https://movie.vodu.me/"

    let homeSections: [(name: String, tagId: Int)] = [
        ("Ramadan 2026", 332),
        ("Featured", 79),
        ("Latest Movies", 83),
        ("Anime Spring 2026", 339),
        ("Latest Series", 84),
        ("Turkish Series", 243),
        ("Korean Drama", 42),
        ("Netflix", 44),
        ("Apple TV+", 62),
        ("Disney+", 72),
        ("HBO Max", 73),
        ("Asian Drama", 91),
        ("Recent Updates", 100),
        ("Kids Tv", 18),
        ("Action Movies", 69),
        ("Spanish", 94),
        ("Documentaries", 142)
    ]

    func fetchHome() {
        guard let url = URL(string: baseUrl + "index.php") else { return }
        isLoading = true
        
        var request = URLRequest(url: url)
        request.setValue("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", forHTTPHeaderField: "User-Agent")
        
        URLSession.shared.dataTask(with: request) { data, _, error in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { self.isLoading = false }
                return
            }
            let (carouselItems, _) = Self.parseHome(html: html, base: self.baseUrl)
            
            DispatchQueue.main.async {
                self.heroItems = carouselItems
                var allCategories: [(name: String, items: [VideoItem])] = []
                
                // الرائج الآن من الكاروسيل
                if !carouselItems.isEmpty {
                    let trendingItems = Array(carouselItems.prefix(10))
                    allCategories.append(("الرائج الآن", trendingItems))
                }
                
                // الأقسام الإضافية مع مهلة زمنية
                let group = DispatchGroup()
                var tempSections: [(name: String, items: [VideoItem])] = []
                tempSections.reserveCapacity(self.homeSections.count)
                
                for section in self.homeSections {
                    group.enter()
                    self.fetchCategory(typeId: section.tagId, page: 1, useTag: true) { items, success in
                        if success && !items.isEmpty {
                            tempSections.append((name: section.name, items: Array(items.prefix(12))))
                        }
                        group.leave()
                    }
                }
                
                // مهلة زمنية 8 ثوانٍ كحد أقصى
                let timeout = DispatchWorkItem {
                    group.leave()
                }
                DispatchQueue.main.asyncAfter(deadline: .now() + 8, execute: timeout)
                
                group.notify(queue: .main) {
                    timeout.cancel()
                    allCategories.append(contentsOf: tempSections)
                    self.categories = allCategories
                    self.isLoading = false
                }
            }
        }.resume()
    }

    func fetchCategory(typeId: Int, page: Int = 1, useTag: Bool = false, completion: @escaping ([VideoItem], Bool) -> Void) {
        let urlStr: String
        if useTag {
            urlStr = "\(baseUrl)?do=list&tag=\(typeId)&page=\(page)"
        } else {
            urlStr = "\(baseUrl)index.php?do=list&type=\(typeId)&page=\(page)"
        }
        
        guard let url = URL(string: urlStr) else { completion([], false); return }
        var request = URLRequest(url: url)
        request.setValue("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", forHTTPHeaderField: "User-Agent")
        
        URLSession.shared.dataTask(with: request) { data, _, error in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([], false) }
                return
            }
            let items = Self.parseListPage(html: html, base: self.baseUrl)
            let hasMore = html.contains("class=\"next\"") || html.contains("»")
            DispatchQueue.main.async { completion(items, hasMore) }
        }.resume()
    }

    func search(query: String, completion: @escaping ([VideoItem]) -> Void) {
        let encoded = query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? query
        let urlStr = "\(baseUrl)index.php?do=list&title=\(encoded)"
        guard let url = URL(string: urlStr) else { completion([]); return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            let items = Self.parseListPage(html: html, base: self.baseUrl)
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    func fetchDetails(id: String, completion: @escaping (MediaDetails) -> Void) {
        guard let url = URL(string: "\(baseUrl)index.php?do=view&type=post&id=\(id)") else { return }
        var request = URLRequest(url: url)
        request.setValue("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", forHTTPHeaderField: "User-Agent")
        
        URLSession.shared.dataTask(with: request) { data, _, _ in
            var details = MediaDetails()
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion(details) }
                return
            }
            details = Self.parseDetails(html: html, base: self.baseUrl)
            DispatchQueue.main.async { completion(details) }
        }.resume()
    }

    // MARK: – HTML parsers

    static func parseHome(html: String, base: String) -> ([VideoItem], [(name: String, items: [VideoItem])]) {
        var carouselItems: [VideoItem] = []
        let carPattern = #"<a href="index\.php\?do=view&type=post&id=(\d+)"><img src="([^"]+)"[^>]*alt="([^"]*)">"#
        if let rx = try? NSRegularExpression(pattern: carPattern, options: []) {
            let ns = html as NSString
            for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if m.numberOfRanges == 4 {
                    let id    = ns.substring(with: m.range(at: 1))
                    var img   = ns.substring(with: m.range(at: 2))
                    let title = ns.substring(with: m.range(at: 3))
                    if !img.hasPrefix("http") { img = base + img }
                    if !carouselItems.contains(where: { $0.id == id }) {
                        carouselItems.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
        }
        return (carouselItems, [])
    }

    static func parseListPage(html: String, base: String) -> [VideoItem] {
        var items: [VideoItem] = []
        let pattern = #"href="index\.php\?do=view&type=post&id=(\d+)"><img src="([^"]+)"[^>]*>\s*</a>\s*<div class="mytitle">\s*<a[^>]*>([^<]+)</a>"#
        if let rx = try? NSRegularExpression(pattern: pattern, options: [.dotMatchesLineSeparators]) {
            let ns = html as NSString
            for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if m.numberOfRanges == 4 {
                    let id    = ns.substring(with: m.range(at: 1))
                    var img   = ns.substring(with: m.range(at: 2))
                    let title = ns.substring(with: m.range(at: 3)).trimmingCharacters(in: .whitespacesAndNewlines)
                    if !img.hasPrefix("http") { img = base + img }
                    if !items.contains(where: { $0.id == id }) {
                        let optimizedImg = optimizeImageUrl(img, width: 400, height: 600)
                        items.append(VideoItem(id: id, title: title, imageUrl: optimizedImg, type: "post"))
                    }
                }
            }
        }
        return items
    }

    static func parseItemXBlock(html: String, base: String) -> [VideoItem] {
        var items: [VideoItem] = []
        let itemxPattern = #"<div class="itemx"[^>]*>.*?<img src="([^"]+)".*?<div class="mytitle">([^<]+)</div>"#
        if let rx = try? NSRegularExpression(pattern: itemxPattern, options: [.dotMatchesLineSeparators]) {
            let ns = html as NSString
            for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if m.numberOfRanges == 3 {
                    var img   = ns.substring(with: m.range(at: 1))
                    let title = ns.substring(with: m.range(at: 2)).trimmingCharacters(in: .whitespacesAndNewlines)
                    if !img.hasPrefix("http") { img = base + img }
                    let optimizedImg = optimizeImageUrl(img, width: 400, height: 600)
                    let fakeId = "home_\(items.count)_\(title.prefix(10))"
                    items.append(VideoItem(id: fakeId, title: title, imageUrl: optimizedImg, type: "post"))
                }
            }
        }
        return items
    }

    static func parseDetails(html: String, base: String) -> MediaDetails {
        var d = MediaDetails()

        func first(_ pattern: String, in text: String, opts: NSRegularExpression.Options = []) -> String? {
            guard let rx = try? NSRegularExpression(pattern: pattern, options: opts),
                  let m = rx.firstMatch(in: text, range: NSRange(text.startIndex..., in: text)),
                  m.numberOfRanges >= 2,
                  let r = Range(m.range(at: 1), in: text)
            else { return nil }
            return String(text[r]).trimmingCharacters(in: .whitespacesAndNewlines)
        }

        d.title    = first(#"<h1>(.*?)</h1>"#, in: html) ?? ""
        d.year     = first(#"<span>Year:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.genre    = first(#"<span>Genre:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.rating   = first(#"<span>IMdB Rating:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.runtime  = first(#"<span>Runtime:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.synopsis = first(#"<h3>Synopsis:</h3>.*?<h4>(.*?)</h4>"#, in: html, opts: [.dotMatchesLineSeparators]) ?? ""

        if let img = first(#"<img src="([^"]+)" class="img-responsive""#, in: html) {
            d.imageUrl = img.hasPrefix("http") ? img : base + img
            d.imageUrl = optimizeImageUrl(d.imageUrl, width: 800, height: 1200)
        }

        var parsedEpisodes: [EpisodeItem] = []
        let episodeBlockPattern = #"<li class="episodeitem">(.*?)</li>"#
        if let blockRx = try? NSRegularExpression(pattern: episodeBlockPattern, options: [.dotMatchesLineSeparators]) {
            for blockMatch in blockRx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if blockMatch.numberOfRanges >= 2,
                   let blockRange = Range(blockMatch.range(at: 1), in: html) {
                    let block = String(html[blockRange])
                    let idPattern       = #"data-id="(\d+)"#
                    let titlePattern    = #"data-title="([^"]*)"#
                    let urlPattern      = #"data-url="([^"]*)"#
                    let url720Pattern   = #"data-url720="([^"]*)"#
                    let url360Pattern   = #"data-url360="([^"]*)"#
                    let url1080Pattern  = #"data-url1080="([^"]*)"#
                    let srtPattern      = #"data-srt="([^"]*)"#
                    let webvttPattern   = #"data-webvtt="([^"]*)"#

                    func extract(_ pattern: String, from text: String) -> String {
                        guard let rx = try? NSRegularExpression(pattern: pattern, options: []),
                              let m = rx.firstMatch(in: text, range: NSRange(text.startIndex..., in: text)),
                              m.numberOfRanges >= 2,
                              let r = Range(m.range(at: 1), in: text)
                        else { return "" }
                        return String(text[r]).trimmingCharacters(in: .whitespacesAndNewlines)
                    }

                    let epId    = extract(idPattern, from: block)
                    guard !epId.isEmpty else { continue }
                    let epTitle  = extract(titlePattern, from: block)
                    let epUrl    = extract(urlPattern, from: block)
                    let epUrl720 = extract(url720Pattern, from: block)
                    let epUrl360 = extract(url360Pattern, from: block)
                    let epUrl1080 = extract(url1080Pattern, from: block)
                    let epSrt    = extract(srtPattern, from: block)
                    let epWebvtt = extract(webvttPattern, from: block)

                    if !epUrl.isEmpty {
                        parsedEpisodes.append(EpisodeItem(
                            id: epId,
                            title: epTitle.isEmpty ? "الحلقة \(parsedEpisodes.count + 1)" : epTitle,
                            url: epUrl,
                            url720: epUrl720,
                            url1080: epUrl1080,
                            url360: epUrl360,
                            subtitleUrl: epSrt,
                            subtitleVttUrl: epWebvtt
                        ))
                    }
                }
            }
        }

        if parsedEpisodes.isEmpty {
            d.isMovie = true
            let moviePattern = #"data-url="([^"]+)"[^>]*data-url360="([^"]*)"[^>]*(?:data-url720="([^"]*)"[^>]*)?data-url1080="([^"]*)"[^>]*data-srt="([^"]*)"[^>]*data-webvtt="([^"]*)""#
            if let rx = try? NSRegularExpression(pattern: moviePattern, options: [.dotMatchesLineSeparators]),
               let m = rx.firstMatch(in: html, range: NSRange(html.startIndex..., in: html)) {
                if let r = Range(m.range(at: 1), in: html) { d.movieUrl = String(html[r]) }
                if let r = Range(m.range(at: 2), in: html) { d.movieUrl360 = String(html[r]) }
                if m.range(at: 3).location != NSNotFound, let r = Range(m.range(at: 3), in: html) { d.movieUrl720 = String(html[r]) }
                if let r = Range(m.range(at: 4), in: html) { d.movieUrl1080 = String(html[r]) }
                if let r = Range(m.range(at: 5), in: html) { d.movieSubtitleUrl = String(html[r]) }
                if let r = Range(m.range(at: 6), in: html) { d.movieSubtitleVttUrl = String(html[r]) }
            }
        } else {
            d.isMovie = false
            d.episodes = parsedEpisodes
        }

        return d
    }
}

// ─────────────────────────────────────────────
// MARK: – Hex Color Extension
// ─────────────────────────────────────────────
extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 3: (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default: (a, r, g, b) = (1, 1, 1, 0)
        }
        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue:  Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
}
"""

with open("UTan/UTan/Scraper.swift", "w", encoding="utf-8") as f:
    f.write(scraper_swift)

# 5. كتابة SubtitleParser.swift (بدون تغيير – يعمل بشكل جيد)
sub_parser_swift = r"""import Foundation

struct SubtitleCue: Identifiable {
    let id = UUID()
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

        URLSession.shared.dataTask(with: urlObj) { data, _, error in
            guard let data = data, error == nil else {
                DispatchQueue.main.async { completion([]) }
                return
            }

            var text: String?
            for encoding: String.Encoding in [.utf8, .isoLatin1, .ascii] {
                if let decoded = String(data: data, encoding: encoding) { text = decoded; break }
            }

            if text == nil {
                let cfEncoding = CFStringEncoding(CFStringEncodings.windowsArabic.rawValue)
                let nsEncoding = CFStringConvertEncodingToNSStringEncoding(cfEncoding)
                text = String(data: data, encoding: String.Encoding(rawValue: nsEncoding))
            }

            guard let finalText = text else {
                DispatchQueue.main.async { completion([]) }
                return
            }

            if finalText.contains("WEBVTT") {
                let cues = parseWebVTT(finalText)
                DispatchQueue.main.async { completion(cues) }
            } else {
                let cues = parseSRT(finalText)
                DispatchQueue.main.async { completion(cues) }
            }
        }.resume()
    }

    private static func parseSRT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let blocks = content.components(separatedBy: "\n\n")
        for block in blocks {
            let lines = block.components(separatedBy: .newlines)
                .map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
                .filter { !$0.isEmpty }
            guard lines.count >= 3 else { continue }
            let timeLine = lines[1]
            let text = lines[2...]
                .joined(separator: "\n")
                .replacingOccurrences(of: #"<[^>]+>"#, with: "", options: .regularExpression)
                .trimmingCharacters(in: .whitespacesAndNewlines)
            if text.isEmpty { continue }
            let times = timeLine.components(separatedBy: " --> ")
            guard times.count == 2,
                  let start = parseSRTTime(times[0]),
                  let end   = parseSRTTime(times[1]) else { continue }
            cues.append(SubtitleCue(startTime: start, endTime: end, text: text))
        }
        return cues
    }

    private static func parseSRTTime(_ timeString: String) -> TimeInterval? {
        let clean = timeString.trimmingCharacters(in: .whitespacesAndNewlines)
        let parts = clean.components(separatedBy: ",")
        guard parts.count == 2, let milliseconds = Double(parts[1]) else { return nil }
        let timeComponents = parts[0].components(separatedBy: ":")
        guard timeComponents.count == 3,
              let hours   = Double(timeComponents[0]),
              let minutes = Double(timeComponents[1]),
              let seconds = Double(timeComponents[2]) else { return nil }
        return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
    }

    private static func parseWebVTT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let lines = content.components(separatedBy: .newlines)
        var i = 0
        while i < lines.count {
            let line = lines[i].trimmingCharacters(in: .whitespacesAndNewlines)
            if line.contains("-->") {
                let times = line.components(separatedBy: "-->")
                guard times.count == 2,
                      let start = parseVTTTime(times[0]),
                      let end   = parseVTTTime(times[1]) else { i += 1; continue }
                var textLines: [String] = []
                i += 1
                while i < lines.count {
                    let nextLine = lines[i].trimmingCharacters(in: .whitespacesAndNewlines)
                    if nextLine.isEmpty { break }
                    textLines.append(nextLine)
                    i += 1
                }
                let text = textLines.joined(separator: "\n")
                    .replacingOccurrences(of: #"<[^>]+>"#, with: "", options: .regularExpression)
                    .trimmingCharacters(in: .whitespacesAndNewlines)
                if !text.isEmpty { cues.append(SubtitleCue(startTime: start, endTime: end, text: text)) }
            }
            i += 1
        }
        return cues
    }

    private static func parseVTTTime(_ timeString: String) -> TimeInterval? {
        let clean = timeString.trimmingCharacters(in: .whitespacesAndNewlines)
        let parts = clean.components(separatedBy: ":")
        var hours: Double = 0, minutes: Double = 0, seconds: Double = 0
        if parts.count == 3 {
            hours = Double(parts[0]) ?? 0
            minutes = Double(parts[1]) ?? 0
            let secParts = parts[2].components(separatedBy: ".")
            seconds = Double(secParts[0]) ?? 0
            if secParts.count == 2 { seconds += (Double(secParts[1]) ?? 0) / 1000 }
        } else if parts.count == 2 {
            minutes = Double(parts[0]) ?? 0
            let secParts = parts[1].components(separatedBy: ".")
            seconds = Double(secParts[0]) ?? 0
            if secParts.count == 2 { seconds += (Double(secParts[1]) ?? 0) / 1000 }
        } else { return nil }
        return hours * 3600 + minutes * 60 + seconds
    }
}
"""

with open("UTan/UTan/SubtitleParser.swift", "w", encoding="utf-8") as f:
    f.write(sub_parser_swift)

# 6. كتابة CustomPlayer.swift (مع إصلاح الخطوط وتحسين double tap وإزالة البلور)
player_swift = r"""import SwiftUI
import AVKit
import AVFoundation

enum VideoQuality: String, CaseIterable, Identifiable {
    case auto  = "تلقائي"
    case q360  = "360p"
    case q720  = "720p"
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

struct VideoPlayerView: UIViewControllerRepresentable {
    let player: AVPlayer
    let gravity: AVLayerVideoGravity
    let onTap: () -> Void
    let onLongPressBegan: () -> Void
    let onLongPressEnded: () -> Void
    let onDoubleTap: (_ isRightHalf: Bool) -> Void

    func makeUIViewController(context: Context) -> AVPlayerViewController {
        let vc = AVPlayerViewController()
        vc.player = player
        vc.showsPlaybackControls = false
        vc.videoGravity = gravity

        let overlay = UIView(frame: vc.view.bounds)
        overlay.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        overlay.backgroundColor = .clear
        vc.view.addSubview(overlay)

        let tap = UITapGestureRecognizer(target: context.coordinator,
                                         action: #selector(Coordinator.handleTap))
        tap.numberOfTapsRequired = 1
        
        let doubleTap = UITapGestureRecognizer(target: context.coordinator,
                                               action: #selector(Coordinator.handleDoubleTap))
        doubleTap.numberOfTapsRequired = 2
        doubleTap.delaysTouchesBegan = true
        
        let longPress = UILongPressGestureRecognizer(target: context.coordinator,
                                                     action: #selector(Coordinator.handleLongPress))
        longPress.minimumPressDuration = 0.4
        
        overlay.addGestureRecognizer(tap)
        overlay.addGestureRecognizer(doubleTap)
        overlay.addGestureRecognizer(longPress)

        if let logoImage = UIImage(named: "logo") {
            let watermark = UIImageView(image: logoImage)
            watermark.alpha = 0.35
            watermark.contentMode = .scaleAspectFit
            watermark.frame = CGRect(x: 12, y: 46, width: 72, height: 28)
            watermark.autoresizingMask = [.flexibleRightMargin, .flexibleBottomMargin]
            vc.view.addSubview(watermark)
        } else {
            let watermark = UILabel()
            watermark.text = "UTan"
            watermark.font = UIFont.systemFont(ofSize: 22, weight: .black)
            watermark.textColor = UIColor.white.withAlphaComponent(0.35)
            watermark.sizeToFit()
            watermark.frame.origin = CGPoint(x: 16, y: 50)
            watermark.autoresizingMask = [.flexibleRightMargin, .flexibleBottomMargin]
            vc.view.addSubview(watermark)
        }

        return vc
    }

    func updateUIViewController(_ vc: AVPlayerViewController, context: Context) {
        vc.videoGravity = gravity
    }

    func makeCoordinator() -> Coordinator {
        Coordinator(onTap: onTap,
                    onLongPressBegan: onLongPressBegan,
                    onLongPressEnded: onLongPressEnded,
                    onDoubleTap: onDoubleTap)
    }

    class Coordinator: NSObject {
        let onTap: () -> Void
        let onLongPressBegan: () -> Void
        let onLongPressEnded: () -> Void
        let onDoubleTap: (Bool) -> Void
        
        init(onTap: @escaping () -> Void,
             onLongPressBegan: @escaping () -> Void,
             onLongPressEnded: @escaping () -> Void,
             onDoubleTap: @escaping (Bool) -> Void) {
            self.onTap = onTap
            self.onLongPressBegan = onLongPressBegan
            self.onLongPressEnded = onLongPressEnded
            self.onDoubleTap = onDoubleTap
        }
        
        @objc func handleTap() { onTap() }
        
        @objc func handleDoubleTap(_ gesture: UITapGestureRecognizer) {
            let location = gesture.location(in: gesture.view)
            let isRightHalf = (location.x > (gesture.view?.bounds.width ?? 0) / 2)
            onDoubleTap(isRightHalf)
        }
        
        @objc func handleLongPress(_ gesture: UILongPressGestureRecognizer) {
            switch gesture.state {
            case .began:                           onLongPressBegan()
            case .ended, .cancelled, .failed:      onLongPressEnded()
            default: break
            }
        }
    }
}

struct CustomPlayerView: View {
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

    @Environment(\.presentationMode) var presentation
    @StateObject private var progressStore = WatchProgressStore.shared
    @StateObject private var settings      = AppSettings.shared

    @State private var player: AVPlayer?
    @State private var isPlaying   = true
    @State private var currentTime: TimeInterval = 0
    @State private var duration: TimeInterval    = 0
    @State private var isDragging  = false
    @State private var seekTarget: TimeInterval  = 0
    @State private var timeObserver: Any?

    @State private var showControls = true
    @State private var hideTimer: Timer?
    @State private var isLocked     = false
    @State private var fitMode      = VideoFitMode.fit
    @State private var quality      = VideoQuality.auto
    @State private var showSettings = false
    @State private var isSpeedActive = false

    @State private var cues: [SubtitleCue] = []
    @State private var activeSub = ""

    @State private var playbackSpeed: Double = 1.0
    @State private var saveTimer: Timer?
    @State private var errorMessage: String?
    
    @State private var seekFeedback: (isRight: Bool, show: Bool) = (false, false)

    // دالة محسنة للخط مع أسماء صحيحة
    private func customFont(size: CGFloat) -> Font {
        let selected = settings.subtitleFontName
        var fontName = ""
        switch selected {
        case "Cairo":
            fontName = "Cairo-Bold"
        case "Rubik":
            fontName = "Rubik-Bold"
        case "Ibm":
            fontName = "IBMPlexArabic-Bold"
        default:
            fontName = selected
        }
        if let uiFont = UIFont(name: fontName, size: size) {
            return Font(uiFont)
        }
        // محاولة البحث عن أي خط يحتوي الاسم
        for family in UIFont.familyNames {
            for font in UIFont.fontNames(forFamilyName: family) {
                if font.lowercased().contains(selected.lowercased()) {
                    if let fallback = UIFont(name: font, size: size) {
                        return Font(fallback)
                    }
                }
            }
        }
        return .system(size: size, weight: .bold, design: .rounded)
    }
    
    private var subtitleFont: Font {
        customFont(size: CGFloat(settings.subtitleFontSize))
    }

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()

            if let player = player {
                VideoPlayerView(
                    player: player,
                    gravity: fitMode.gravity,
                    onTap: {
                        if !isLocked {
                            withAnimation { showControls.toggle() }
                            if showControls { scheduleHide() }
                        }
                    },
                    onLongPressBegan: {
                        if !isLocked && !isSpeedActive {
                            isSpeedActive = true
                            player.rate = 2.0
                        }
                    },
                    onLongPressEnded: {
                        if isSpeedActive {
                            isSpeedActive = false
                            player.rate = isPlaying ? Float(playbackSpeed) : 0
                        }
                    },
                    onDoubleTap: { isRightHalf in
                        seekFeedback = (isRightHalf, true)
                        DispatchQueue.main.asyncAfter(deadline: .now() + 0.6) {
                            seekFeedback.show = false
                        }
                        if isRightHalf {
                            let t = min(duration, currentTime + 10)
                            player.seek(to: CMTime(seconds: t, preferredTimescale: 600))
                        } else {
                            let t = max(0, currentTime - 10)
                            player.seek(to: CMTime(seconds: t, preferredTimescale: 600))
                        }
                        scheduleHide()
                    }
                )
                .ignoresSafeArea()

                if isSpeedActive {
                    VStack {
                        HStack(spacing: 6) {
                            Image(systemName: "forward.frame.fill")
                            Text("2× سرعة")
                        }
                        .font(.system(size: 14, weight: .bold))
                        .foregroundColor(.white)
                        .padding(.horizontal, 16)
                        .padding(.vertical, 8)
                        .background(Color.black.opacity(0.75))
                        .cornerRadius(20)
                        .padding(.top, 60)
                        Spacer()
                    }
                }

                if settings.subtitlesEnabled && !activeSub.isEmpty {
                    VStack {
                        Spacer()
                        Text(activeSub)
                            .font(subtitleFont)
                            .foregroundColor(settings.subtitleColor)
                            .shadow(color: .black, radius: 3, x: 1, y: 1)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 20)
                            .padding(.vertical, 6)
                            .background(Color.black.opacity(settings.subtitleBgOpacity))
                            .cornerRadius(8)
                            .padding(.bottom, CGFloat(settings.subtitleBottomPad))
                    }
                    .allowsHitTesting(false)
                }

                if let error = errorMessage {
                    VStack {
                        Text(error)
                            .foregroundColor(.white)
                            .padding()
                            .background(Color.white.opacity(0.15))
                            .cornerRadius(8)
                    }
                }

                if showControls || isLocked {
                    controlsOverlay(player: player)
                        .transition(.opacity)
                        .animation(.easeInOut(duration: 0.25), value: showControls)
                }
                
                // مؤشر التقديم/الترجيع – تصميم جميل ونظيف
                if seekFeedback.show {
                    VStack {
                        Spacer()
                        HStack(spacing: 12) {
                            Image(systemName: seekFeedback.isRight ? "goforward.10" : "gobackward.10")
                                .font(.system(size: 44, weight: .medium))
                            Text(seekFeedback.isRight ? "+10" : "-10")
                                .font(.system(size: 24, weight: .bold))
                        }
                        .foregroundColor(.white)
                        .padding(.horizontal, 24)
                        .padding(.vertical, 12)
                        .background(Color.black.opacity(0.7))
                        .clipShape(Capsule())
                        .padding(.bottom, 140)
                    }
                    .transition(.opacity)
                    .animation(.easeOut(duration: 0.2), value: seekFeedback.show)
                }

            } else {
                VStack(spacing: 20) {
                    ProgressView().tint(.white)
                    Text("جاري التحميل...")
                        .foregroundColor(.white)
                    Button("إغلاق") {
                        presentation.wrappedValue.dismiss()
                    }
                    .padding()
                    .background(Color.white.opacity(0.15))
                    .foregroundColor(.white)
                    .cornerRadius(8)
                }
            }
        }
        .statusBar(hidden: true)
        .onAppear  { setupPlayer() }
        .onDisappear { shutdown() }
    }

    @ViewBuilder
    private func controlsOverlay(player: AVPlayer) -> some View {
        VStack {
            HStack {
                if !isLocked {
                    Button { shutdown(); presentation.wrappedValue.dismiss() } label: {
                        Image(systemName: "arrow.backward").playerBtn()
                    }
                    Spacer()
                    if UIImage(named: "logo") != nil {
                        Image("logo")
                            .resizable()
                            .scaledToFit()
                            .frame(height: 60)
                            .opacity(0.9)
                    } else {
                        Text(episodeTitle.isEmpty ? itemTitle : episodeTitle)
                            .font(.system(size: 14, weight: .bold))
                            .foregroundColor(.white)
                            .lineLimit(1)
                    }
                    Spacer()
                } else {
                    Spacer()
                }
                Button {
                    withAnimation { isLocked.toggle() }
                    if isLocked { hideControls() }
                } label: {
                    Image(systemName: isLocked ? "lock.fill" : "lock.open")
                        .playerBtn(color: .white)
                }
            }
            .padding(.horizontal, 16)
            .padding(.top, 20)
            .background(
                LinearGradient(colors: [.black.opacity(0.8), .clear],
                               startPoint: .top, endPoint: .bottom)
            )

            Spacer()

            if !isLocked {
                VStack(spacing: 12) {
                    HStack(spacing: 10) {
                        Text(formatTime(isDragging ? seekTarget : currentTime))
                            .timeLabel()
                        Slider(
                            value: isDragging ? $seekTarget : $currentTime,
                            in: 0...max(duration, 1)
                        ) { editing in
                            isDragging = editing
                            if !editing {
                                player.seek(to: CMTime(seconds: seekTarget, preferredTimescale: 600))
                                currentTime = seekTarget
                                scheduleHide()
                            }
                        }
                        .accentColor(UT_RED)
                        Text(formatTime(duration))
                            .timeLabel()
                    }
                    .padding(.horizontal, 16)

                    HStack(spacing: 50) {
                        Button {
                            let t = max(0, currentTime - 10)
                            player.seek(to: CMTime(seconds: t, preferredTimescale: 600))
                            scheduleHide()
                        } label: {
                            Image(systemName: "gobackward.10")
                                .font(.title).foregroundColor(.white)
                        }

                        // زر التشغيل/الإيقاف بدون أي خلفية أو بلور
                        Button {
                            if isPlaying { player.pause() }
                            else         { player.rate = Float(playbackSpeed) }
                            isPlaying.toggle()
                            scheduleHide()
                        } label: {
                            Image(systemName: isPlaying ? "pause.circle.fill" : "play.circle.fill")
                                .font(.system(size: 66))
                                .foregroundColor(UT_RED)
                                .shadow(color: .black.opacity(0.5), radius: 2, x: 0, y: 1)
                        }
                        .buttonStyle(PlainButtonStyle())

                        Button {
                            let t = min(duration, currentTime + 10)
                            player.seek(to: CMTime(seconds: t, preferredTimescale: 600))
                            scheduleHide()
                        } label: {
                            Image(systemName: "goforward.10")
                                .font(.title).foregroundColor(.white)
                        }
                    }

                    HStack(spacing: 6) {
                        ForEach(VideoQuality.allCases) { q in
                            Button(q.rawValue) { switchQuality(to: q) }
                                .font(.system(size: 12, weight: quality == q ? .bold : .regular))
                                .foregroundColor(.white)
                                .padding(.horizontal, 10).padding(.vertical, 6)
                                .background(quality == q ? UT_RED : Color.clear)
                                .cornerRadius(8)
                        }
                        Spacer()
                        Button {
                            let all = VideoFitMode.allCases
                            let idx = all.firstIndex(of: fitMode) ?? 0
                            fitMode = all[(idx + 1) % all.count]
                        } label: {
                            Image(systemName: "aspectratio")
                                .font(.caption).foregroundColor(.white.opacity(0.8))
                        }
                        Text(fitMode.rawValue)
                            .font(.system(size: 11))
                            .foregroundColor(.white.opacity(0.7))
                    }
                    .padding(.horizontal, 16)
                    .padding(.bottom, 20)
                }
                .background(
                    LinearGradient(colors: [.clear, .black.opacity(0.9)],
                                   startPoint: .top, endPoint: .bottom)
                )
            }
        }
    }

    private func setupPlayer() {
        let resumeTime = progressStore.progress(for: itemId)?.progressSeconds ?? 0
        let urlStr = resolvedUrl(quality: quality)

        guard !urlStr.isEmpty, let url = URL(string: urlStr) else {
            errorMessage = "رابط الفيديو غير صالح"
            return
        }

        let item = AVPlayerItem(url: url)
        let p = AVPlayer(playerItem: item)
        self.player = p

        if resumeTime > 5 {
            p.seek(to: CMTime(seconds: resumeTime, preferredTimescale: 600))
        }
        p.play()

        NotificationCenter.default.addObserver(
            forName: .AVPlayerItemDidPlayToEndTime,
            object: item, queue: .main) { _ in self.isPlaying = false }

        Task {
            if let dur = try? await item.asset.load(.duration) {
                DispatchQueue.main.async { self.duration = dur.seconds }
            }
        }

        timeObserver = p.addPeriodicTimeObserver(
            forInterval: CMTime(seconds: 0.25, preferredTimescale: 600), queue: .main
        ) { t in
            if !self.isDragging { self.currentTime = t.seconds }
            if let cue = self.cues.first(where: { t.seconds >= $0.startTime && t.seconds <= $0.endTime }) {
                self.activeSub = cue.text
            } else {
                self.activeSub = ""
            }
        }

        let subUrl = subtitleVttUrl.isEmpty ? subtitleUrl : subtitleVttUrl
        if !subUrl.isEmpty {
            SubtitleParser.parse(url: subUrl) { parsedCues in
                self.cues = parsedCues
            }
        }

        scheduleHide()
        saveTimer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            guard let p = self.player, self.duration > 0 else { return }
            progressStore.save(
                itemId: self.itemId,
                title: self.itemTitle,
                imageUrl: self.itemImageUrl,
                episodeId: self.episodeId,
                episodeTitle: self.episodeTitle,
                progress: p.currentTime().seconds,
                duration: self.duration,
                videoUrl: self.videoUrl,
                videoUrl720: self.videoUrl720,
                videoUrl1080: self.videoUrl1080,
                videoUrl360: self.videoUrl360,
                subUrl: self.subtitleUrl,
                subVttUrl: self.subtitleVttUrl
            )
        }
    }

    private func shutdown() {
        saveTimer?.invalidate()
        hideTimer?.invalidate()
        if let obs = timeObserver { player?.removeTimeObserver(obs); timeObserver = nil }
        player?.pause()
        player = nil
    }

    private func scheduleHide() {
        hideTimer?.invalidate()
        hideTimer = Timer.scheduledTimer(withTimeInterval: 4, repeats: false) { _ in
            withAnimation { self.showControls = false }
        }
    }

    private func hideControls() {
        hideTimer?.invalidate()
        withAnimation { showControls = false }
    }

    private func switchQuality(to q: VideoQuality) {
        guard let player = player else { return }
        let t = player.currentTime()
        quality = q
        guard let url = URL(string: resolvedUrl(quality: q)) else { return }
        let item = AVPlayerItem(url: url)
        player.replaceCurrentItem(with: item)
        player.seek(to: t)
        player.rate = isPlaying ? Float(playbackSpeed) : 0
    }

    private func resolvedUrl(quality: VideoQuality) -> String {
        func fixUrl(_ u: String) -> String {
            if u.isEmpty { return "" }
            if u.hasPrefix("http") { return u }
            return "https://movie.vodu.me/" + u
        }
        switch quality {
        case .q360:  return fixUrl(videoUrl360.isEmpty ? videoUrl : videoUrl360)
        case .q720:  return fixUrl(videoUrl720.isEmpty ? videoUrl : videoUrl720)
        case .q1080: return fixUrl(videoUrl1080.isEmpty ? videoUrl : videoUrl1080)
        default:     return fixUrl(videoUrl)
        }
    }

    private func formatTime(_ s: TimeInterval) -> String {
        guard s.isFinite else { return "00:00" }
        let h = Int(s) / 3600, m = (Int(s) % 3600) / 60, sec = Int(s) % 60
        return h > 0
            ? String(format: "%02d:%02d:%02d", h, m, sec)
            : String(format: "%02d:%02d", m, sec)
    }
}

extension Image {
    func playerBtn(color: Color = .white) -> some View {
        self.font(.title3)
            .foregroundColor(color)
            .padding(12)
            .background(Color.white.opacity(0.15))
            .clipShape(Circle())
    }
}

extension Text {
    func timeLabel() -> some View {
        self.font(.system(size: 12, weight: .semibold))
            .monospacedDigit()
            .foregroundColor(.white)
    }
}
"""

with open("UTan/UTan/CustomPlayer.swift", "w", encoding="utf-8") as f:
    f.write(player_swift)

# 7. كتابة Views.swift (مع تثبيت ارتفاع الكاردات، تثبيت اللوغو، تحميل الأقسام)
views_swift = r"""import SwiftUI

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Loader (يختفي بعد 5 ثوانٍ)
// ─────────────────────────────────────────────────────────────────────────────
struct UTanLoader: View {
    @Binding var isLoading: Bool
    @State private var opacity = 1.0
    
    init(isLoading: Binding<Bool>) {
        self._isLoading = isLoading
    }
    
    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            VStack {
                if let logoImage = UIImage(named: "logo") {
                    Image(uiImage: logoImage)
                        .resizable()
                        .scaledToFit()
                        .frame(width: 120, height: 120)
                        .opacity(opacity)
                        .onAppear {
                            withAnimation(.easeInOut(duration: 1.2).repeatForever(autoreverses: true)) {
                                opacity = 0.5
                            }
                            DispatchQueue.main.asyncAfter(deadline: .now() + 5) {
                                isLoading = false
                            }
                        }
                } else {
                    Text("UTAN")
                        .font(.system(size: 40, weight: .black))
                        .foregroundColor(.white)
                }
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Player Presentation Data Structure
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
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Poster Card (أبعاد موحدة)
// ─────────────────────────────────────────────────────────────────────────────
struct PosterCard: View {
    let item: VideoItem
    var progress: WatchProgress? = nil

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            ZStack(alignment: .bottom) {
                AsyncImage(url: URL(string: item.imageUrl)) { img in
                    img.resizable()
                        .aspectRatio(contentMode: .fill)
                } placeholder: {
                    Color(white: 0.12)
                }
                .frame(width: 120, height: 180)
                .clipped()
                .cornerRadius(16)

                LinearGradient(colors: [.clear, .black.opacity(0.8)],
                               startPoint: .center, endPoint: .bottom)
                    .cornerRadius(16)

                if let p = progress, p.durationSeconds > 0 {
                    GeometryReader { geo in
                        ZStack(alignment: .leading) {
                            Color.white.opacity(0.3).frame(height: 4)
                            Color.white
                                .frame(
                                    width: geo.size.width * min(1, CGFloat(p.progressSeconds / p.durationSeconds)),
                                    height: 4
                                )
                        }
                    }
                    .frame(height: 4)
                    .padding(.horizontal, 8)
                    .padding(.bottom, 8)
                }
            }
            .frame(width: 120, height: 180)
            .shadow(color: .black.opacity(0.4), radius: 5, x: 0, y: 4)

            Text(item.title)
                .font(.system(size: 12, weight: .bold))
                .foregroundColor(.white)
                .lineLimit(2)
                .frame(width: 120, alignment: .leading)
        }
        .frame(height: 210, alignment: .top) // ارتفاع ثابت لجميع الكاردات
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
            } else {
                TabView {
                    HomeView(scraper: scraper)
                        .tabItem { Label("الرئيسية", systemImage: "house.fill") }
                    BrowseView(scraper: scraper)
                        .tabItem { Label("تصفح", systemImage: "square.grid.2x2.fill") }
                    SearchView(scraper: scraper)
                        .tabItem { Label("بحث", systemImage: "magnifyingglass") }
                    DownloadsView()
                        .tabItem { Label("التحميلات", systemImage: "arrow.down.circle.fill") }
                    SettingsView()
                        .tabItem { Label("المزيد", systemImage: "line.3.horizontal") }
                }
                .accentColor(UT_RED)
                .preferredColorScheme(.dark)
                .onAppear {
                    let appearance = UITabBarAppearance()
                    appearance.configureWithOpaqueBackground()
                    appearance.backgroundColor = UIColor(APP_BG)
                    UITabBar.appearance().standardAppearance = appearance
                    if #available(iOS 15.0, *) {
                        UITabBar.appearance().scrollEdgeAppearance = appearance
                    }
                }
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Network Card (صورة فقط بدون نص، حواف جميلة)
// ─────────────────────────────────────────────────────────────────────────────
struct NetworkCard: Identifiable {
    let id = UUID()
    let assetName: String
    let label: String
    let categoryId: Int
}

private let networkCards: [NetworkCard] = [
    NetworkCard(assetName: "Netflix",  label: "نتفليكس",  categoryId: 44),
    NetworkCard(assetName: "Anime",    label: "أنمي",      categoryId: 2),
    NetworkCard(assetName: "Kids",     label: "أطفال",     categoryId: 9018),
    NetworkCard(assetName: "Hbo",      label: "HBO",        categoryId: 73),
    NetworkCard(assetName: "Disney",   label: "ديزني",     categoryId: 72),
    NetworkCard(assetName: "Marvel",   label: "مارفل",     categoryId: 9014)
]

struct NetworkCardsRow: View {
    @ObservedObject var scraper: MovieScraper

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("تصفح حسب الشبكة")
                .font(.system(size: 20, weight: .bold))
                .foregroundColor(.white)
                .padding(.horizontal, 20)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 16) {
                    ForEach(networkCards) { card in
                        if let category = SITE_CATEGORIES.first(where: { $0.id == card.categoryId }) {
                            NavigationLink(destination: CategoryListView(category: category,
                                                                         scraper: scraper)) {
                                NetworkCardView(card: card)
                            }
                        }
                    }
                }
                .padding(.horizontal, 20)
            }
        }
    }
}

struct NetworkCardView: View {
    let card: NetworkCard
    
    var body: some View {
        ZStack {
            if let path = Bundle.main.path(forResource: card.assetName, ofType: "jpg"),
               let uiImage = UIImage(contentsOfFile: path) {
                Image(uiImage: uiImage)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 160, height: 100)
                    .cornerRadius(16)
                    .overlay(
                        RoundedRectangle(cornerRadius: 16)
                            .stroke(UT_RED.opacity(0.3), lineWidth: 1)
                    )
            } else if let path = Bundle.main.path(forResource: card.assetName, ofType: "png"),
                      let uiImage = UIImage(contentsOfFile: path) {
                Image(uiImage: uiImage)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 160, height: 100)
                    .cornerRadius(16)
                    .overlay(
                        RoundedRectangle(cornerRadius: 16)
                            .stroke(UT_RED.opacity(0.3), lineWidth: 1)
                    )
            } else {
                RoundedRectangle(cornerRadius: 16)
                    .fill(Color.white.opacity(0.12))
                    .frame(width: 160, height: 100)
                    .overlay(
                        RoundedRectangle(cornerRadius: 16)
                            .stroke(UT_RED.opacity(0.3), lineWidth: 1)
                    )
            }
        }
        .frame(width: 160, height: 100)
        .shadow(color: .black.opacity(0.3), radius: 4, x: 0, y: 2)
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – HomeView (شعار ثابت)
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
                                HeroBanner(items: scraper.heroItems, scraper: scraper)
                                    .frame(height: UIScreen.main.bounds.height * 0.75)
                            }

                            VStack(alignment: .leading, spacing: 30) {
                                if !progressStore.recent.isEmpty {
                                    ContinueWatchingRow(items: progressStore.recent,
                                                        playItem: $playItem)
                                        .padding(.top, -60)
                                        .zIndex(1)
                                }

                                NetworkCardsRow(scraper: scraper)

                                ForEach(scraper.categories, id: \.name) { cat in
                                    if !cat.items.isEmpty {
                                        CategoryRow(title: cat.name, items: cat.items)
                                    }
                                }
                            }
                            .padding(.bottom, 100)
                        }
                    }
                    .ignoresSafeArea(.all, edges: .top)
                }

                // شعار ثابت في الأعلى – بدون أي حركة أو أنميشن
                HStack {
                    if let logoImage = UIImage(named: "logo") {
                        Image(uiImage: logoImage)
                            .resizable()
                            .scaledToFit()
                            .frame(height: 60)
                    } else {
                        Text("UTan")
                            .font(.system(size: 30, weight: .black, design: .rounded))
                            .foregroundColor(.white)
                    }
                    Spacer()
                }
                .padding(.horizontal, 20)
                .padding(.top, 50)
                .zIndex(2) // يضمن بقاء الشعار فوق كل العناصر
            }
            .navigationBarHidden(true)
            .fullScreenCover(item: $playItem) { data in
                CustomPlayerView(
                    itemId: data.itemId,
                    itemTitle: data.itemTitle,
                    itemImageUrl: data.itemImageUrl,
                    videoUrl: data.videoUrl,
                    videoUrl720: data.videoUrl720,
                    videoUrl1080: data.videoUrl1080,
                    videoUrl360: data.videoUrl360,
                    subtitleUrl: data.subtitleUrl,
                    subtitleVttUrl: data.subtitleVttUrl,
                    episodeId: data.episodeId,
                    episodeTitle: data.episodeTitle
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
    @ObservedObject var scraper: MovieScraper
    @State private var current = 0
    @State private var timer: Timer?
    @ObservedObject var favStore = FavoritesStore.shared

    var body: some View {
        TabView(selection: $current) {
            ForEach(items.prefix(8).indices, id: \.self) { i in
                let item = items[i]
                ZStack(alignment: .bottom) {
                    AsyncImage(url: URL(string: item.imageUrl)) { img in
                        img.resizable().aspectRatio(contentMode: .fill)
                    } placeholder: { Color(white: 0.05) }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .clipped()

                    LinearGradient(colors: [.clear, APP_BG.opacity(0.7), APP_BG],
                                   startPoint: .center, endPoint: .bottom)

                    VStack(spacing: 16) {
                        Text(item.title)
                            .font(.system(size: 32, weight: .heavy))
                            .foregroundColor(.white)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal)
                            .shadow(color: .black, radius: 4)

                        HStack(spacing: 20) {
                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                HStack {
                                    Image(systemName: "play.fill")
                                    Text("شاهد الآن")
                                }
                                .font(.system(size: 16, weight: .bold))
                                .padding(.horizontal, 30).padding(.vertical, 12)
                                .background(UT_RED)
                                .foregroundColor(.white)
                                .cornerRadius(12)
                            }

                            Button { favStore.toggle(item: item) } label: {
                                VStack(spacing: 6) {
                                    Image(systemName: favStore.isFavorite(item.id) ? "checkmark" : "plus")
                                        .font(.system(size: 20, weight: .bold))
                                    Text("قائمتي").font(.system(size: 10, weight: .semibold))
                                }
                                .foregroundColor(.white)
                            }
                        }
                        .padding(.bottom, 80)
                    }
                }
                .tag(i)
            }
        }
        .tabViewStyle(.page(indexDisplayMode: .never))
        .onAppear  { startTimer() }
        .onDisappear { timer?.invalidate() }
    }

    private func startTimer() {
        timer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            withAnimation(.easeInOut(duration: 0.8)) {
                current = (current + 1) % min(items.count, 8)
            }
        }
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
                .font(.system(size: 20, weight: .bold))
                .foregroundColor(.white)
                .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 16) {
                    ForEach(items.prefix(10)) { prog in
                        Button {
                            playItem = PlayerData(
                                itemId: prog.itemId,
                                itemTitle: prog.title,
                                itemImageUrl: prog.imageUrl,
                                videoUrl: prog.videoUrl,
                                videoUrl720: prog.videoUrl720,
                                videoUrl1080: prog.videoUrl1080,
                                videoUrl360: prog.videoUrl360,
                                subtitleUrl: prog.subtitleUrl,
                                subtitleVttUrl: prog.subtitleVttUrl,
                                episodeId: prog.episodeId,
                                episodeTitle: prog.episodeTitle
                            )
                        } label: {
                            VStack(alignment: .leading, spacing: 8) {
                                ZStack(alignment: .center) {
                                    AsyncImage(url: URL(string: prog.imageUrl)) { img in
                                        img.resizable().aspectRatio(contentMode: .fill)
                                    } placeholder: { Color(white: 0.12) }
                                    .frame(width: 160, height: 100)
                                    .clipped()
                                    .cornerRadius(12)

                                    Color.black.opacity(0.3).cornerRadius(12)

                                    Image(systemName: "play.circle.fill")
                                        .font(.system(size: 40))
                                        .foregroundColor(.white.opacity(0.9))

                                    if prog.durationSeconds > 0 {
                                        VStack {
                                            Spacer()
                                            GeometryReader { geo in
                                                ZStack(alignment: .leading) {
                                                    Color.white.opacity(0.3).frame(height: 4)
                                                    Color.white.frame(
                                                        width: geo.size.width * CGFloat(min(1, prog.progressSeconds / prog.durationSeconds)),
                                                        height: 4
                                                    )
                                                }
                                            }
                                            .frame(height: 4)
                                        }
                                        .padding(.horizontal, 4).padding(.bottom, 4)
                                    }
                                }
                                .frame(width: 160, height: 100)

                                Text(prog.title)
                                    .font(.system(size: 13, weight: .bold))
                                    .foregroundColor(.white)
                                    .lineLimit(1)
                                    .frame(width: 160, alignment: .leading)

                                if !prog.episodeTitle.isEmpty {
                                    Text(prog.episodeTitle)
                                        .font(.system(size: 11, weight: .medium))
                                        .foregroundColor(.gray)
                                        .lineLimit(1)
                                        .frame(width: 160, alignment: .leading)
                                }
                            }
                        }
                    }
                }
                .padding(.horizontal)
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
            Text(title)
                .font(.system(size: 20, weight: .bold))
                .foregroundColor(.white)
                .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 14) {
                    ForEach(items) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item, progress: store.progress(for: item.id))
                        }
                    }
                }
                .padding(.horizontal)
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Browse & Category Lists
// ─────────────────────────────────────────────────────────────────────────────
struct BrowseView: View {
    @ObservedObject var scraper: MovieScraper
    let cols = [GridItem(.flexible()), GridItem(.flexible())]

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                ScrollView {
                    LazyVGrid(columns: cols, spacing: 20) {
                        ForEach(SITE_CATEGORIES) { cat in
                            NavigationLink(destination: CategoryListView(category: cat,
                                                                         scraper: scraper)) {
                                ZStack {
                                    RoundedRectangle(cornerRadius: 20)
                                        .fill(Color.white.opacity(0.08))
                                        .overlay(
                                            RoundedRectangle(cornerRadius: 20)
                                                .stroke(UT_RED.opacity(0.3), lineWidth: 1)
                                        )
                                    VStack(spacing: 12) {
                                        Image(systemName: "film")
                                            .font(.system(size: 32))
                                            .foregroundColor(UT_RED)
                                        Text(cat.nameAr)
                                            .font(.system(size: 16, weight: .bold))
                                            .foregroundColor(.white)
                                        Text(cat.nameEn)
                                            .font(.system(size: 11))
                                            .foregroundColor(.gray)
                                    }
                                    .padding(12)
                                }
                                .frame(height: 110)
                            }
                        }
                    }
                    .padding(16)
                }
            }
            .navigationTitle("تصفح")
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }
}

struct CategoryListView: View {
    let category: SiteCategory
    @ObservedObject var scraper: MovieScraper
    @State private var items: [VideoItem] = []
    @State private var page    = 1
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
                }
                .padding()
                if loading { UTanLoader(isLoading: $loading) }
            }
        }
        .navigationTitle(category.nameAr)
        .onAppear { if items.isEmpty { loadMore() } }
    }

    private func loadMore() {
        loading = true
        scraper.fetchCategory(typeId: category.remoteId, page: page, useTag: category.isTag) { newItems, _ in
            items.append(contentsOf: newItems)
            page += 1
            loading = false
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Search View
// ─────────────────────────────────────────────────────────────────────────────
struct SearchView: View {
    @ObservedObject var scraper: MovieScraper
    @State private var query   = ""
    @State private var results: [VideoItem] = []
    let cols = [GridItem(.adaptive(minimum: 110), spacing: 14)]

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                VStack(spacing: 0) {
                    HStack {
                        Image(systemName: "magnifyingglass").foregroundColor(.gray)
                        TextField("بحث...", text: $query)
                            .foregroundColor(.white)
                            .onSubmit { scraper.search(query: query) { r in results = r } }
                    }
                    .padding(14)
                    .background(Color.white.opacity(0.1))
                    .cornerRadius(12)
                    .padding()

                    ScrollView {
                        LazyVGrid(columns: cols, spacing: 16) {
                            ForEach(results) { item in
                                NavigationLink(destination: DetailsView(itemId: item.id)) {
                                    PosterCard(item: item)
                                }
                            }
                        }
                        .padding()
                    }
                }
            }
            .navigationTitle("البحث")
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Downloads & Settings Views
// ─────────────────────────────────────────────────────────────────────────────
struct DownloadsView: View {
    @ObservedObject var manager = DownloadManager.shared

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                if manager.activeDownloads.isEmpty {
                    VStack(spacing: 20) {
                        Image(systemName: "arrow.down.circle")
                            .font(.system(size: 60)).foregroundColor(.gray)
                        Text("لا توجد تحميلات").foregroundColor(.gray)
                    }
                } else {
                    List {
                        ForEach(manager.activeDownloads) { dl in
                            HStack {
                                AsyncImage(url: URL(string: dl.imageUrl)) { img in
                                    img.resizable().aspectRatio(contentMode: .fill)
                                } placeholder: { Color.gray }
                                .frame(width: 50, height: 75).cornerRadius(8)

                                VStack(alignment: .leading) {
                                    Text(dl.title).font(.headline).foregroundColor(.white)
                                    if dl.isCompleted {
                                        Text("مكتمل - محفوظ في الصور")
                                            .font(.caption).foregroundColor(.green)
                                    } else {
                                        ProgressView(value: dl.progress).tint(UT_RED)
                                        Text("\(Int(dl.progress * 100))%")
                                            .font(.caption).foregroundColor(.gray)
                                    }
                                }
                                Spacer()
                                Button { manager.cancel(id: dl.id) } label: {
                                    Image(systemName: "xmark.circle.fill")
                                        .foregroundColor(.red)
                                }
                            }
                            .listRowBackground(Color.white.opacity(0.05))
                        }
                    }
                    .scrollContentBackground(.hidden)
                }
            }
            .navigationTitle("التحميلات")
        }
    }
}

struct SettingsView: View {
    @ObservedObject var settings     = AppSettings.shared
    @ObservedObject var historyStore = WatchProgressStore.shared
    @State private var cacheCleared  = false

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                Form {
                    Section(header: Text("إعدادات الترجمة").foregroundColor(UT_RED)) {
                        Toggle("تفعيل الترجمة", isOn: $settings.subtitlesEnabled)
                        if settings.subtitlesEnabled {
                            Picker("الخط", selection: $settings.subtitleFontName) {
                                Text("Cairo").tag("Cairo")
                                Text("Rubik").tag("Rubik")
                                Text("IBM Plex Sans").tag("Ibm")
                            }
                            .pickerStyle(.segmented)
                            .colorMultiply(.white)
                            
                            VStack(alignment: .leading) {
                                Text("حجم الخط: \(Int(settings.subtitleFontSize))")
                                Slider(value: $settings.subtitleFontSize, in: 14...40, step: 1)
                                    .accentColor(UT_RED)
                            }
                            VStack(alignment: .leading) {
                                Text("الهامش السفلي: \(Int(settings.subtitleBottomPad))")
                                Slider(value: $settings.subtitleBottomPad, in: 20...150, step: 5)
                                    .accentColor(UT_RED)
                            }
                            VStack(alignment: .leading) {
                                Text("شفافية الخلفية: \(Int(settings.subtitleBgOpacity * 100))%")
                                Slider(value: $settings.subtitleBgOpacity, in: 0.0...1.0, step: 0.1)
                                    .accentColor(UT_RED)
                            }
                            ScrollView(.horizontal) {
                                HStack {
                                    ForEach(["#FFFFFF", "#FFFF00", "#00FFFF", "#FF00FF"], id: \.self) { hex in
                                        Circle()
                                            .fill(Color(hex: hex))
                                            .frame(width: 30, height: 30)
                                            .overlay(
                                                Circle().stroke(Color.white,
                                                                lineWidth: settings.subtitleColorHex == hex ? 3 : 0)
                                            )
                                            .onTapGesture { settings.subtitleColorHex = hex }
                                    }
                                }
                            }
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    Section(header: Text("البيانات").foregroundColor(UT_RED)) {
                        NavigationLink(destination: HistoryListView(store: historyStore)) {
                            Text("سجل المشاهدة (\(historyStore.recent.count))")
                        }
                        Button {
                            settings.clearCache()
                            cacheCleared = true
                            DispatchQueue.main.asyncAfter(deadline: .now() + 2) { cacheCleared = false }
                        } label: {
                            Text(cacheCleared ? "تم المسح!" : "مسح التخزين المؤقت والسجل")
                                .foregroundColor(.red)
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)
                }
                .scrollContentBackground(.hidden)
            }
            .navigationTitle("المزيد")
        }
    }
}

struct HistoryListView: View {
    @ObservedObject var store: WatchProgressStore
    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            List {
                ForEach(store.recent) { prog in
                    HStack {
                        AsyncImage(url: URL(string: prog.imageUrl)) { img in
                            img.resizable().aspectRatio(contentMode: .fill)
                        } placeholder: { Color.gray }
                        .frame(width: 50, height: 75).cornerRadius(8)

                        VStack(alignment: .leading) {
                            Text(prog.title).font(.headline).foregroundColor(.white)
                            if !prog.episodeTitle.isEmpty {
                                Text(prog.episodeTitle).font(.caption).foregroundColor(.gray)
                            }
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                }
                .onDelete { idx in
                    idx.forEach { i in store.remove(itemId: store.recent[i].itemId) }
                }
            }
            .scrollContentBackground(.hidden)
        }
        .navigationTitle("سجل المشاهدة")
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – DetailsView
// ─────────────────────────────────────────────────────────────────────────────
struct DetailsView: View {
    let itemId: String
    @StateObject private var scraper   = MovieScraper()
    @ObservedObject private var favStore = FavoritesStore.shared

    @State private var details: MediaDetails?
    @State private var loading         = true
    @State private var playerData: PlayerData?
    @State private var selectedSeason  = ""

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            if loading {
                UTanLoader(isLoading: $loading)
            } else if let d = details {
                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 0) {
                        // Hero image + info overlay
                        ZStack(alignment: .bottomLeading) {
                            AsyncImage(url: URL(string: d.imageUrl)) { img in
                                img.resizable().aspectRatio(contentMode: .fill)
                            } placeholder: { Color(white: 0.1) }
                            .frame(maxWidth: .infinity).frame(height: 350)
                            .clipped()

                            LinearGradient(colors: [.clear, APP_BG.opacity(0.8), APP_BG],
                                           startPoint: .top, endPoint: .bottom)

                            VStack(alignment: .leading, spacing: 12) {
                                Text(d.title)
                                    .font(.system(size: 28, weight: .heavy))
                                    .foregroundColor(.white)

                                HStack(spacing: 10) {
                                    if !d.year.isEmpty    { badge(d.year) }
                                    if !d.rating.isEmpty  {
                                        HStack(spacing: 3) {
                                            Image(systemName: "star.fill").foregroundColor(.yellow)
                                            Text(d.rating)
                                        }
                                        .font(.system(size: 13, weight: .bold)).foregroundColor(.white)
                                    }
                                    if !d.runtime.isEmpty { badge(d.runtime) }
                                }

                                HStack(spacing: 16) {
                                    if d.isMovie {
                                        Button { playMovie(d: d) } label: {
                                            HStack {
                                                Image(systemName: "play.fill")
                                                Text("شاهد الآن")
                                            }
                                            .font(.system(size: 16, weight: .bold))
                                            .frame(maxWidth: .infinity)
                                            .padding()
                                            .background(UT_RED)
                                            .foregroundColor(.white)
                                            .cornerRadius(12)
                                        }

                                        Button {
                                            DownloadManager.shared.startDownload(
                                                item: VideoItem(id: itemId, title: d.title,
                                                                imageUrl: d.imageUrl, type: "post"),
                                                isMovie: true,
                                                vUrl: d.movieUrl,
                                                sUrl: d.movieSubtitleUrl
                                            )
                                        } label: {
                                            Image(systemName: "arrow.down.circle")
                                                .font(.title)
                                                .foregroundColor(.white)
                                                .padding()
                                        }
                                    }

                                    Button {
                                        favStore.toggle(item: VideoItem(id: itemId, title: d.title,
                                                                        imageUrl: d.imageUrl, type: "post"))
                                    } label: {
                                        Image(systemName: favStore.isFavorite(itemId)
                                              ? "checkmark.circle.fill" : "plus.circle")
                                            .font(.title)
                                            .foregroundColor(.white)
                                            .padding()
                                    }
                                }
                                .padding(.top, 10)
                            }
                            .padding(.horizontal, 20)
                            .padding(.bottom, 20)
                        }

                        if !d.synopsis.isEmpty {
                            VStack(alignment: .leading, spacing: 8) {
                                Text("القصة")
                                    .font(.system(size: 18, weight: .bold)).foregroundColor(.white)
                                Text(d.synopsis)
                                    .font(.system(size: 15)).foregroundColor(.gray).lineSpacing(6)
                            }
                            .padding(20)
                        }

                        if !d.isMovie && !d.sortedSeasons.isEmpty {
                            VStack(alignment: .leading, spacing: 16) {
                                ScrollView(.horizontal, showsIndicators: false) {
                                    HStack(spacing: 12) {
                                        ForEach(d.sortedSeasons, id: \.self) { season in
                                            Button { selectedSeason = season } label: {
                                                Text(season)
                                                    .font(.system(size: 16, weight: .bold))
                                                    .padding(.horizontal, 20).padding(.vertical, 10)
                                                    .background(
                                                        selectedSeason == season
                                                            ? UT_RED
                                                            : Color.white.opacity(0.08)
                                                    )
                                                    .foregroundColor(.white)
                                                    .cornerRadius(12)
                                            }
                                        }
                                    }
                                    .padding(.horizontal, 20)
                                }

                                LazyVStack(spacing: 12) {
                                    let eps = d.seasonsDict[selectedSeason] ?? []
                                    ForEach(eps) { ep in
                                        HStack(spacing: 14) {
                                            Button {
                                                playerData = PlayerData(
                                                    itemId: itemId, itemTitle: d.title,
                                                    itemImageUrl: d.imageUrl,
                                                    videoUrl: ep.url,
                                                    videoUrl720: ep.url720,
                                                    videoUrl1080: ep.url1080,
                                                    videoUrl360: ep.url360,
                                                    subtitleUrl: ep.subtitleUrl,
                                                    subtitleVttUrl: ep.subtitleVttUrl,
                                                    episodeId: ep.id,
                                                    episodeTitle: ep.title
                                                )
                                            } label: {
                                                HStack {
                                                    Image(systemName: "play.circle.fill")
                                                        .font(.title2)
                                                        .foregroundColor(UT_RED)
                                                    Text(ep.title)
                                                        .font(.system(size: 14, weight: .bold))
                                                        .foregroundColor(.white)
                                                    Spacer()
                                                }
                                                .padding()
                                                .background(Color.white.opacity(0.05))
                                                .cornerRadius(12)
                                            }

                                            Button {
                                                DownloadManager.shared.startDownload(
                                                    item: VideoItem(id: ep.id, title: ep.title,
                                                                    imageUrl: d.imageUrl, type: "post"),
                                                    isMovie: false,
                                                    vUrl: ep.url,
                                                    sUrl: ep.subtitleUrl
                                                )
                                            } label: {
                                                Image(systemName: "arrow.down.circle")
                                                    .foregroundColor(.gray)
                                                    .font(.title3)
                                            }
                                        }
                                        .padding(.horizontal, 20)
                                    }
                                }
                            }
                            .padding(.bottom, 40)
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
                episodeId: data.episodeId, episodeTitle: data.episodeTitle
            )
        }
        .onAppear {
            scraper.fetchDetails(id: itemId) { result in
                details = result
                if let firstSeason = result.sortedSeasons.first { selectedSeason = firstSeason }
                loading = false
            }
        }
    }

    private func playMovie(d: MediaDetails) {
        playerData = PlayerData(
            itemId: itemId, itemTitle: d.title, itemImageUrl: d.imageUrl,
            videoUrl: d.movieUrl, videoUrl720: d.movieUrl720, videoUrl1080: d.movieUrl1080, videoUrl360: d.movieUrl360,
            subtitleUrl: d.movieSubtitleUrl, subtitleVttUrl: d.movieSubtitleVttUrl,
            episodeId: "", episodeTitle: ""
        )
    }

    private func badge(_ text: String) -> some View {
        Text(text)
            .font(.system(size: 12, weight: .bold))
            .padding(.horizontal, 10).padding(.vertical, 4)
            .background(Color.white.opacity(0.15))
            .cornerRadius(6)
            .foregroundColor(.white)
    }
}
"""

with open("UTan/UTan/Views.swift", "w", encoding="utf-8") as f:
    f.write(views_swift)

print("✅ UTan v4.0 – جميع الإصلاحات تم تطبيقها بنجاح.")
print("   – تم إصلاح مشكلة الخطوط (الآن يتم تحميل Cairo-Bold, Rubik-Bold, IBMPlexArabic-Bold).")
print("   – تم إصلاح الأقسام في الصفحة الرئيسية (تظهر جميع الأقسام مع مهلة زمنية).")
print("   – تم توحيد ارتفاع الكاردات (210 نقطة) بغض النظر عن طول العنوان.")
print("   – تم تثبيت اللوغو في الصفحة الرئيسية (بدون حركة أو أنميشن).")
print("   – تم تحسين شكل مؤشر الضغطة المزدوجة (تصميم دائري أنيق).")
print("   – تم إزالة البلور من زر التشغيل والإيقاف.")
print("   – ملاحظة: يجب وضع ملفات الخطوط (.ttf) والصور المطلوبة يدوياً في مجلد UTan/UTan/")