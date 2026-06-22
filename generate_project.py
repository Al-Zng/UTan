import os

# إنشاء بنية المجلدات
os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# ==========================================
# 1. project.pbxproj
# ==========================================
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
\t\t010101012C12345600000040 /* SupabaseManager.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000041 /* SupabaseManager.swift */; };
\t\t010101012C12345600000042 /* AccountViews.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000043 /* AccountViews.swift */; };
\t\t010101012C1234560000001A /* logo.png in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000001B /* logo.png */; };
\t\t010101012C1234560000001C /* Netflix.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000001D /* Netflix.jpg */; };
\t\t010101012C1234560000001E /* Anime.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000001F /* Anime.jpg */; };
\t\t010101012C12345600000020 /* Kids.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000021 /* Kids.jpg */; };
\t\t010101012C12345600000022 /* Hbo.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000023 /* Hbo.jpg */; };
\t\t010101012C12345600000024 /* Disney.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000025 /* Disney.jpg */; };
\t\t010101012C12345600000026 /* Marvel.jpg in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000027 /* Marvel.jpg */; };
\t\t010101012C12345600000030 /* Cairo.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000031 /* Cairo.ttf */; };
\t\t010101012C12345600000032 /* Cairo-Bold-1.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000033 /* Cairo-Bold-1.ttf */; };
\t\t010101012C12345600000034 /* Rubik.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000035 /* Rubik.ttf */; };
\t\t010101012C12345600000036 /* Rubik-Bold.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000037 /* Rubik-Bold.ttf */; };
\t\t010101012C12345600000038 /* Ibm.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000039 /* Ibm.ttf */; };
\t\t010101012C1234560000003A /* IBMPlexArabic-Bold.ttf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000003B /* IBMPlexArabic-Bold.ttf */; };
\t\t010101012C1234560000003C /* alfont_com_AlFont_com_ExpoArabic-Bold.otf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000003D /* alfont_com_AlFont_com_ExpoArabic-Bold.otf */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
\t\t010101012C12345600000002 /* UTanApp.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = UTanApp.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000004 /* Scraper.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Scraper.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000006 /* CustomPlayer.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = CustomPlayer.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000008 /* SubtitleParser.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = SubtitleParser.swift; sourceTree = "<group>"; };
\t\t010101012C1234560000000A /* Views.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Views.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000041 /* SupabaseManager.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = SupabaseManager.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000043 /* AccountViews.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = AccountViews.swift; sourceTree = "<group>"; };
\t\t010101012C1234560000000B /* Info.plist */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
\t\t010101012C1234560000000C /* UTan.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = UTan.app; sourceTree = BUILT_PRODUCTS_DIR; };
\t\t010101012C1234560000001B /* logo.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; path = logo.png; sourceTree = "<group>"; };
\t\t010101012C1234560000001D /* Netflix.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Netflix.jpg; sourceTree = "<group>"; };
\t\t010101012C1234560000001F /* Anime.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Anime.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000021 /* Kids.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Kids.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000023 /* Hbo.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Hbo.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000025 /* Disney.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Disney.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000027 /* Marvel.jpg */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = Marvel.jpg; sourceTree = "<group>"; };
\t\t010101012C12345600000031 /* Cairo.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = Cairo.ttf; sourceTree = "<group>"; };
\t\t010101012C12345600000033 /* Cairo-Bold-1.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "Cairo-Bold-1.ttf"; sourceTree = "<group>"; };
\t\t010101012C12345600000035 /* Rubik.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = Rubik.ttf; sourceTree = "<group>"; };
\t\t010101012C12345600000037 /* Rubik-Bold.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "Rubik-Bold.ttf"; sourceTree = "<group>"; };
\t\t010101012C12345600000039 /* Ibm.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = Ibm.ttf; sourceTree = "<group>"; };
\t\t010101012C1234560000003B /* IBMPlexArabic-Bold.ttf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "IBMPlexArabic-Bold.ttf"; sourceTree = "<group>"; };
\t\t010101012C1234560000003D /* alfont_com_AlFont_com_ExpoArabic-Bold.otf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "alfont_com_AlFont_com_ExpoArabic-Bold.otf"; sourceTree = "<group>"; };
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
\t\t\t\t010101012C12345600000041 /* SupabaseManager.swift */,
\t\t\t\t010101012C12345600000043 /* AccountViews.swift */,
\t\t\t\t010101012C1234560000000B /* Info.plist */,
\t\t\t\t010101012C1234560000001B /* logo.png */,
\t\t\t\t010101012C1234560000001D /* Netflix.jpg */,
\t\t\t\t010101012C1234560000001F /* Anime.jpg */,
\t\t\t\t010101012C12345600000021 /* Kids.jpg */,
\t\t\t\t010101012C12345600000023 /* Hbo.jpg */,
\t\t\t\t010101012C12345600000025 /* Disney.jpg */,
\t\t\t\t010101012C12345600000027 /* Marvel.jpg */,
\t\t\t\t010101012C12345600000031 /* Cairo.ttf */,
\t\t\t\t010101012C12345600000033 /* Cairo-Bold-1.ttf */,
\t\t\t\t010101012C12345600000035 /* Rubik.ttf */,
\t\t\t\t010101012C12345600000037 /* Rubik-Bold.ttf */,
\t\t\t\t010101012C12345600000039 /* Ibm.ttf */,
\t\t\t\t010101012C1234560000003B /* IBMPlexArabic-Bold.ttf */,
\t\t\t\t010101012C1234560000003D /* alfont_com_AlFont_com_ExpoArabic-Bold.otf */,
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
\t\t\t\t010101012C12345600000030 /* Cairo.ttf in Resources */,
\t\t\t\t010101012C12345600000032 /* Cairo-Bold-1.ttf in Resources */,
\t\t\t\t010101012C12345600000034 /* Rubik.ttf in Resources */,
\t\t\t\t010101012C12345600000036 /* Rubik-Bold.ttf in Resources */,
\t\t\t\t010101012C12345600000038 /* Ibm.ttf in Resources */,
\t\t\t\t010101012C1234560000003A /* IBMPlexArabic-Bold.ttf in Resources */,
\t\t\t\t010101012C1234560000003C /* alfont_com_AlFont_com_ExpoArabic-Bold.otf in Resources */,
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
\t\t\t\t010101012C12345600000040 /* SupabaseManager.swift in Sources */,
\t\t\t\t010101012C12345600000042 /* AccountViews.swift in Sources */,
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
\t\t\t\tMARKETING_VERSION = 5.0;
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
\t\t\t\tMARKETING_VERSION = 5.0;
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

# ==========================================
# 2. Info.plist
# ==========================================
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
    <key>CFBundleURLTypes</key>
    <array>
        <dict>
            <key>CFBundleURLSchemes</key>
            <array>
                <string>utan</string>
            </array>
        </dict>
    </array>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>5.0</string>
    <key>CFBundleVersion</key>
    <string>5</string>
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
        <string>audio</string>
    </array>
    <key>UILaunchScreen</key>
    <dict/>
    <key>UISupportedInterfaceOrientations</key>
    <array>
        <string>UIInterfaceOrientationPortrait</string>
        <string>UIInterfaceOrientationLandscapeLeft</string>
        <string>UIInterfaceOrientationLandscapeRight</string>
    </array>
    <key>UISupportedInterfaceOrientations~ipad</key>
    <array>
        <string>UIInterfaceOrientationPortrait</string>
        <string>UIInterfaceOrientationPortraitUpsideDown</string>
        <string>UIInterfaceOrientationLandscapeLeft</string>
        <string>UIInterfaceOrientationLandscapeRight</string>
    </array>
    <key>UIUserInterfaceStyle</key>
    <string>Dark</string>
    <key>UIAppFonts</key>
    <array>
        <string>Cairo.ttf</string>
        <string>Cairo-Bold-1.ttf</string>
        <string>Rubik.ttf</string>
        <string>Rubik-Bold.ttf</string>
        <string>Ibm.ttf</string>
        <string>IBMPlexArabic-Bold.ttf</string>
        <string>alfont_com_AlFont_com_ExpoArabic-Bold.otf</string>
    </array>
</dict>
</plist>
"""
with open("UTan/UTan/Info.plist", "w", encoding="utf-8") as f:
    f.write(info_plist)

# ==========================================
# 3. UTanApp.swift
# ==========================================
app_swift = """import SwiftUI

@main
struct UTanApp: App {
    @StateObject private var settings = AppSettings.shared

    var body: some Scene {
        WindowGroup {
            MainTabView()
                .environmentObject(settings)
                .environment(\\.layoutDirection, settings.appLanguage == "en" ? .leftToRight : .rightToLeft)
        }
    }
}
"""
with open("UTan/UTan/UTanApp.swift", "w", encoding="utf-8") as f:
    f.write(app_swift)

# ==========================================
# 4. Scraper.swift
# ==========================================
scraper_swift = r"""import Foundation
import SwiftUI
import UIKit
import Network

// ─────────────────────────────────────────────
// MARK: – Global Colors & Configs
// ─────────────────────────────────────────────
var APP_BG: Color {
    switch AppSettings.shared.appTheme {
    case "amoled":      return Color.black
    case "dark_blue":   return Color(red: 0.03, green: 0.05, blue: 0.14)
    case "dark_purple": return Color(red: 0.06, green: 0.03, blue: 0.13)
    default:            return Color(red: 0.05, green: 0.02, blue: 0.09) // dark (افتراضي)
    }
}

var UT_RED: Color {
    switch AppSettings.shared.accentColorName {
    case "blue":   return Color(red: 0.10, green: 0.40, blue: 0.90)
    case "orange": return Color(red: 0.95, green: 0.45, blue: 0.05)
    case "green":  return Color(red: 0.10, green: 0.78, blue: 0.35)
    case "pink":   return Color(red: 0.90, green: 0.20, blue: 0.55)
    default:       return Color(red: 0.89, green: 0.04, blue: 0.08) // red (افتراضي)
    }
}

func L(_ ar: String, _ en: String) -> String {
    AppSettings.shared.appLanguage == "en" ? en : ar
}

let UT_WHITE   = Color.white
let UT_SURFACE = Color.white.opacity(0.12)
let UT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

// ─────────────────────────────────────────────
// MARK: – AppSettings Store
// ─────────────────────────────────────────────
final class AppSettings: ObservableObject {
    static let shared = AppSettings()

    @AppStorage("sub_fontSize")   var subtitleFontSize: Double  = 22.0
    @AppStorage("sub_colorHex")   var subtitleColorHex: String  = "#FFFFFF"
    @AppStorage("sub_bgOpacity")  var subtitleBgOpacity: Double = 0.6
    @AppStorage("sub_bottomPad")  var subtitleBottomPad: Double = 60.0
    @AppStorage("sub_enabled")    var subtitlesEnabled: Bool    = true
    @AppStorage("sub_fontName")   var subtitleFontName: String  = "Expo" // تم تعيين إكسبو كافتراضي للترجمة
    @AppStorage("sub_delay")      var subtitleDelay: Double     = 0.0

    @AppStorage("autoplay_next")      var autoPlayNextEnabled: Bool = true
    @AppStorage("autoplay_countdown") var autoPlayCountdownSeconds: Int = 10

    @AppStorage("pref_quality") var preferredQuality: String = "تلقائي"
    @AppStorage("download_wifi_only") var downloadOverWifiOnly: Bool = false

    @AppStorage("app_language") var appLanguage: String = "ar"
    @AppStorage("app_theme") var appTheme: String = "dark"
    @AppStorage("accent_color") var accentColorName: String = "red"
    @AppStorage("grid_size") var gridSizeStr: String = "medium"

    var subtitleColor: Color { Color(hex: subtitleColorHex) }

    func clearCache() {
        URLCache.shared.removeAllCachedResponses()
        WatchProgressStore.shared.clearAll()
    }
}

// ─────────────────────────────────────────────
// MARK: – Custom Fonts System
// ─────────────────────────────────────────────
func utFont(_ keyword: String, size: CGFloat, bold: Bool = false) -> Font {
    let key = keyword.lowercased()

    if key == "system" {
        return .system(size: size, weight: bold ? .bold : .regular, design: .default)
    }

    func familyMatches(_ family: String) -> Bool {
        let f = family.lowercased()
        switch key {
        case "ibm":    return f.contains("ibm") || f.contains("plex")
        case "rubik":  return f.contains("rubik")
        case "expo":   return f.contains("expo") || f.contains("alfont")
        default:       return f.contains("cairo")
        }
    }

    for family in UIFont.familyNames where familyMatches(family) {
        let names = UIFont.fontNames(forFamilyName: family)
        let chosen: String?
        if bold {
            chosen = names.first(where: { $0.lowercased().contains("bold") }) ?? names.first
        } else {
            chosen = names.first(where: { !$0.lowercased().contains("bold") }) ?? names.first
        }
        if let n = chosen, let uiFont = UIFont(name: n, size: size) {
            return Font(uiFont)
        }
    }

    let fallbackNames: [String]
    switch key {
    case "ibm":   fallbackNames = ["IBMPlexArabic-Bold","IBMPlexSansArabic-Regular","Ibm"]
    case "rubik": fallbackNames = ["Rubik-Bold","Rubik-Regular","Rubik"]
    case "expo":  fallbackNames = ["alfont_com_AlFont_com_ExpoArabic-Bold","ExpoArabic-Bold"]
    default:      fallbackNames = ["Cairo-Bold-1","Cairo-Regular","Cairo"]
    }
    for n in fallbackNames {
        if let uiFont = UIFont(name: n, size: size) { return Font(uiFont) }
    }

    return .system(size: size, weight: bold ? .bold : .regular)
}

/// الخط الرئيسي للتطبيق: إكسبو العربي كخط افتراضي أساسي، وSystem للإنجليزية
func appFont(_ size: CGFloat, bold: Bool = false) -> Font {
    AppSettings.shared.appLanguage == "ar"
        ? utFont("expo", size: size, bold: bold)
        : .system(size: size, weight: bold ? .bold : .regular)
}

func subtitleFontForPlayer(name: String, size: CGFloat) -> Font {
    switch name.lowercased() {
    case "expo":   return utFont("expo", size: size, bold: true)
    case "ibm":    return utFont("ibm", size: size, bold: true)
    case "rubik":  return utFont("rubik", size: size, bold: true)
    case "system": return .system(size: size, weight: .bold)
    default:       return utFont("cairo", size: size, bold: true)
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
    let url4k: String
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

    var episodeNumber: Int? {
        let pattern = "(?i)E(\\d+)"
        guard let rx = try? NSRegularExpression(pattern: pattern),
              let match = rx.firstMatch(in: title, range: NSRange(location: 0, length: title.count)),
              match.numberOfRanges >= 2 else { return nil }
        let nsString = title as NSString
        return Int(nsString.substring(with: match.range(at: 1)))
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
    var movieUrl4k: String = ""
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

    func nextEpisode(after episodeId: String) -> EpisodeItem? {
        guard let idx = episodes.firstIndex(where: { $0.id == episodeId }) else { return nil }
        let next = idx + 1
        guard next < episodes.count else { return nil }
        return episodes[next]
    }

    func episode(withId id: String) -> EpisodeItem? {
        episodes.first(where: { $0.id == id })
    }
}

// ─────────────────────────────────────────────
// MARK: – Watch Progress & Favorites Stores
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
    var videoUrl4k: String = ""
    var subtitleUrl: String = ""
    var subtitleVttUrl: String = ""
    var isMovie: Bool = true
}

final class WatchProgressStore: ObservableObject {
    static let shared = WatchProgressStore()
    private let key = "UTanWatchProgress_v3"

    @Published var allProgress: [String: WatchProgress] = [:]

    private init() { load() }

    func save(itemId: String, title: String, imageUrl: String,
              episodeId: String, episodeTitle: String,
              progress: Double, duration: Double,
              videoUrl: String, videoUrl720: String, videoUrl1080: String, videoUrl360: String, videoUrl4k: String = "",
              subUrl: String, subVttUrl: String, isMovie: Bool = true) {
        let record = WatchProgress(
            itemId: itemId, title: title, imageUrl: imageUrl,
            episodeId: episodeId, episodeTitle: episodeTitle,
            progressSeconds: progress, durationSeconds: duration,
            updatedAt: Date(),
            videoUrl: videoUrl, videoUrl720: videoUrl720, videoUrl1080: videoUrl1080, videoUrl360: videoUrl360, videoUrl4k: videoUrl4k,
            subtitleUrl: subUrl, subtitleVttUrl: subVttUrl, isMovie: isMovie
        )
        allProgress[itemId] = record
        persist()
        if AuthSession.shared.isLoggedIn {
            SupabaseManager.shared.upsertProgress(record) { _ in }
        }
    }

    func remove(itemId: String) {
        allProgress.removeValue(forKey: itemId)
        persist()
        if AuthSession.shared.isLoggedIn {
            SupabaseManager.shared.deleteProgress(itemId: itemId) { _ in }
        }
    }

    func clearAll() {
        allProgress.removeAll()
        persist()
    }

    func mergeFromCloud(_ remote: [WatchProgress]) {
        for r in remote {
            if let local = allProgress[r.itemId] {
                if r.updatedAt > local.updatedAt { allProgress[r.itemId] = r }
            } else {
                allProgress[r.itemId] = r
            }
        }
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

    func persist() {
        if let data = try? JSONEncoder().encode(allProgress) {
            UserDefaults.standard.set(data, forKey: key)
        }
    }
}

final class FavoritesStore: ObservableObject {
    static let shared = FavoritesStore()
    private let key = "UTanFavorites_v1"

    @Published var items: [VideoItem] = []

    private init() { load() }

    func toggle(item: VideoItem) {
        if let idx = items.firstIndex(where: { $0.id == item.id }) {
            items.remove(at: idx)
            persist()
            if AuthSession.shared.isLoggedIn {
                SupabaseManager.shared.deleteFavorite(itemId: item.id) { _ in }
            }
        } else {
            items.insert(item, at: 0)
            persist()
            if AuthSession.shared.isLoggedIn {
                SupabaseManager.shared.upsertFavorite(item: item) { _ in }
            }
        }
    }

    func isFavorite(_ id: String) -> Bool {
        items.contains(where: { $0.id == id })
    }

    func mergeFromCloud(_ remote: [VideoItem]) {
        let localIds = Set(items.map { $0.id })
        for item in remote where !localIds.contains(item.id) {
            items.append(item)
        }
        persist()
    }

    private func load() {
        if let data = UserDefaults.standard.data(forKey: key),
           let decoded = try? JSONDecoder().decode([VideoItem].self, from: data) {
            items = decoded
        }
    }
    func persist() {
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

final class NetworkMonitor: ObservableObject {
    static let shared = NetworkMonitor()
    @Published var isOnWifi: Bool = true
    private let monitor = NWPathMonitor()

    private init() {
        monitor.pathUpdateHandler = { [weak self] path in
            DispatchQueue.main.async {
                self?.isOnWifi = path.usesInterfaceType(.wifi)
            }
        }
        monitor.start(queue: DispatchQueue(label: "UTanNetworkMonitor"))
    }
}

final class ImageCacheManager {
    static let shared = ImageCacheManager()
    let cache = NSCache<NSString, UIImage>()
    private init() {
        cache.countLimit = 300
        cache.totalCostLimit = 120 * 1024 * 1024
    }
}

enum CachedImagePhase {
    case empty
    case success(Image)
    case failure

    var image: Image? {
        if case .success(let img) = self { return img }
        return nil
    }

    var error: Error? {
        if case .failure = self { return URLError(.badServerResponse) }
        return nil
    }
}

struct CachedAsyncImage<Content: View>: View {
    let url: URL?
    @ViewBuilder var content: (CachedImagePhase) -> Content

    @State private var phase: CachedImagePhase = .empty

    var body: some View {
        content(phase)
            .onAppear { load() }
    }

    private func load() {
        guard let url = url else { phase = .failure; return }
        let key = url.absoluteString as NSString
        if let cached = ImageCacheManager.shared.cache.object(forKey: key) {
            phase = .success(Image(uiImage: cached))
            return
        }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let uiImage = UIImage(data: data) else {
                DispatchQueue.main.async { self.phase = .failure }
                return
            }
            ImageCacheManager.shared.cache.setObject(uiImage, forKey: key, cost: data.count)
            DispatchQueue.main.async {
                self.phase = .success(Image(uiImage: uiImage))
            }
        }.resume()
    }
}

final class DownloadManager: NSObject, ObservableObject, URLSessionDownloadDelegate {
    static let shared = DownloadManager()
    private let key = "UTanDownloads_v1"

    @Published var activeDownloads: [DownloadTaskItem] = []
    @Published var lastError: String?
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
        if AppSettings.shared.downloadOverWifiOnly && !NetworkMonitor.shared.isOnWifi {
            DispatchQueue.main.async {
                self.lastError = "التنزيل عبر الواي فاي فقط مفعّل، اتصل بشبكة واي فاي للمتابعة"
            }
            return
        }
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
// MARK: – Site Categories Map
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

func optimizeImageUrl(_ url: String, width: Int = 400, height: Int = 600) -> String {
    if url.contains("w=750") || url.contains("h=388") { return url }
    let separator = url.contains("?") ? "&" : "?"
    return "\(url)\(separator)w=\(width)&h=\(height)&crop-to-fit"
}

// ─────────────────────────────────────────────
// MARK: – Main Scraper / Network Layer
// ─────────────────────────────────────────────
final class MovieScraper: ObservableObject {
    @Published var heroItems: [VideoItem] = []
    @Published var categories: [(name: String, items: [VideoItem], tagId: Int)] = []
    @Published var allItemsPool: [VideoItem] = []
    @Published var isLoading = false

    let baseUrl = "https://movie.vodu.me/"

    func fetchHome() {
        guard let url = URL(string: baseUrl + "index.php") else { return }
        isLoading = true

        var request = URLRequest(url: url)
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")

        URLSession.shared.dataTask(with: request) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { self.isLoading = false }
                return
            }

            let (carouselItems, sections) = Self.parseHomePage(html: html, base: self.baseUrl)

            DispatchQueue.main.async {
                self.heroItems = carouselItems
                var allCategories: [(name: String, items: [VideoItem], tagId: Int)] = []

                if !carouselItems.isEmpty {
                    let trendingItems = Array(carouselItems.prefix(10))
                    allCategories.append(("الرائج الآن", trendingItems, -1))
                }

                allCategories.append(contentsOf: sections)
                self.categories = allCategories
                self.isLoading = false

                var pool: [VideoItem] = []
                for cat in allCategories { pool.append(contentsOf: cat.items) }
                self.allItemsPool = pool
            }
        }.resume()
    }

    func refreshHome(completion: (() -> Void)? = nil) {
        guard let url = URL(string: baseUrl + "index.php") else { completion?(); return }
        var request = URLRequest(url: url)
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")
        URLSession.shared.dataTask(with: request) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion?() }
                return
            }
            let (carouselItems, sections) = Self.parseHomePage(html: html, base: self.baseUrl)
            DispatchQueue.main.async {
                self.heroItems = carouselItems
                var allCategories: [(name: String, items: [VideoItem], tagId: Int)] = []
                if !carouselItems.isEmpty {
                    allCategories.append(("الرائج الآن", Array(carouselItems.prefix(10)), -1))
                }
                allCategories.append(contentsOf: sections)
                self.categories = allCategories
                completion?()
            }
        }.resume()
    }

    func fetchCategory(typeId: Int, page: Int = 1, useTag: Bool = false, sort: String? = nil, genre: String? = nil, completion: @escaping ([VideoItem], Bool) -> Void) {
        var urlStr: String
        let pageParam = page > 1 ? "&page=\(page)" : ""
        if useTag {
            urlStr = "\(baseUrl)index.php?do=list&tag=\(typeId)\(pageParam)"
        } else {
            urlStr = "\(baseUrl)index.php?do=list&type=\(typeId)\(pageParam)"
        }
        if let s = sort, !s.isEmpty { urlStr += "&sort=\(s)" }
        if let g = genre, !g.isEmpty { urlStr += "&genre=\(g)" }
        guard let url = URL(string: urlStr) else { completion([], false); return }
        var request = URLRequest(url: url)
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")

        URLSession.shared.dataTask(with: request) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([], false) }
                return
            }
            let items = Self.parseListPage(html: html, base: self.baseUrl)
            let hasMore = Self.detectHasMorePages(html: html, currentPage: page)
            DispatchQueue.main.async { completion(items, hasMore) }
        }.resume()
    }

    private static func detectHasMorePages(html: String, currentPage: Int) -> Bool {
        guard let startRange = html.range(of: "<ul class=\"pagination\">") else { return false }
        let afterStart = html[startRange.upperBound...]
        guard let endRange = afterStart.range(of: "</ul>") else { return false }
        let block = String(afterStart[..<endRange.lowerBound])
        guard let regex = try? NSRegularExpression(pattern: #"page=(\d+)"#) else { return false }
        let matches = regex.matches(in: block, range: NSRange(block.startIndex..., in: block))
        let pageNumbers = matches.compactMap { m -> Int? in
            guard let r = Range(m.range(at: 1), in: block) else { return nil }
            return Int(block[r])
        }
        return (pageNumbers.max() ?? currentPage) > currentPage
    }

    func advancedSearch(title: String? = nil, genre: String? = nil, type: String? = nil,
                        imdb: String? = nil, director: String? = nil, writer: String? = nil,
                        cast: String? = nil, year: String? = nil, mpr: String? = nil,
                        imdbrate: String? = nil, production: String? = nil,
                        language: String? = nil, featured: Bool? = nil,
                        completion: @escaping ([VideoItem]) -> Void) {
        var components = URLComponents(string: baseUrl + "index.php")!
        var queryItems: [URLQueryItem] = [URLQueryItem(name: "do", value: "list")]
        if let t = title, !t.isEmpty { queryItems.append(URLQueryItem(name: "title", value: t)) }
        if let g = genre, !g.isEmpty { queryItems.append(URLQueryItem(name: "genre", value: g)) }
        if let tp = type, !tp.isEmpty { queryItems.append(URLQueryItem(name: "type", value: tp)) }
        if let im = imdb, !im.isEmpty { queryItems.append(URLQueryItem(name: "imdb", value: im)) }
        if let d = director, !d.isEmpty { queryItems.append(URLQueryItem(name: "director", value: d)) }
        if let w = writer, !w.isEmpty { queryItems.append(URLQueryItem(name: "writer", value: w)) }
        if let c = cast, !c.isEmpty { queryItems.append(URLQueryItem(name: "cast", value: c)) }
        if let y = year, !y.isEmpty { queryItems.append(URLQueryItem(name: "year", value: y)) }
        if let m = mpr, !m.isEmpty { queryItems.append(URLQueryItem(name: "mpr", value: m)) }
        if let r = imdbrate, !r.isEmpty { queryItems.append(URLQueryItem(name: "imdbrate", value: r)) }
        if let p = production, !p.isEmpty { queryItems.append(URLQueryItem(name: "production", value: p)) }
        if let l = language, !l.isEmpty { queryItems.append(URLQueryItem(name: "language", value: l)) }
        if let f = featured, f { queryItems.append(URLQueryItem(name: "featured", value: "1")) }
        components.queryItems = queryItems
        guard let url = components.url else { completion([]); return }
        var request = URLRequest(url: url)
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")
        URLSession.shared.dataTask(with: request) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            let items = Self.parseListPage(html: html, base: self.baseUrl)
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    func search(query: String, completion: @escaping ([VideoItem]) -> Void) {
        advancedSearch(title: query, completion: completion)
    }

    func fetchDetails(id: String, completion: @escaping (MediaDetails) -> Void) {
        guard let url = URL(string: "\(baseUrl)index.php?do=view&type=post&id=\(id)") else { return }
        var request = URLRequest(url: url)
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")

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

    static func parseHomePage(html: String, base: String) -> ([VideoItem], [(name: String, items: [VideoItem], tagId: Int)]) {
        let ns = html as NSString
        var carouselItems: [VideoItem] = []
        let carPattern = #"<a href="index\.php\?do=view&type=post&id=(\d+)"><img src="([^"]+)"[^>]*alt="([^"]*)">"#
        if let rx = try? NSRegularExpression(pattern: carPattern, options: []) {
            for m in rx.matches(in: html, range: NSRange(location: 0, length: ns.length)) {
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

        var sections: [(name: String, items: [VideoItem], tagId: Int)] = []
        let headerPattern = #"<h2><a href="\?do=list&tag=(\d+)"[^>]*>([^<]+)</a></h2>"#
        let itemPattern   = #"<a href="index\.php\?do=view&type=post&id=(\d+)">\s*<img src="([^"]+)"[^>]*>\s*<div class="mytitle">([^<]*)</div>"#

        guard let headerRx = try? NSRegularExpression(pattern: headerPattern, options: []),
              let itemRx   = try? NSRegularExpression(pattern: itemPattern, options: [.dotMatchesLineSeparators])
        else { return (carouselItems, sections) }

        let headerMatches = headerRx.matches(in: html, range: NSRange(location: 0, length: ns.length))

        for (idx, header) in headerMatches.enumerated() {
            guard header.numberOfRanges == 3 else { continue }
            let tagId = Int(ns.substring(with: header.range(at: 1))) ?? -1
            let title = ns.substring(with: header.range(at: 2)).trimmingCharacters(in: .whitespacesAndNewlines)

            let blockStart = header.range.location + header.range.length
            let blockEnd: Int = (idx + 1 < headerMatches.count) ? headerMatches[idx + 1].range.location : ns.length
            guard blockStart < blockEnd else { continue }

            let block = ns.substring(with: NSRange(location: blockStart, length: blockEnd - blockStart))
            let blockNS = block as NSString

            var items: [VideoItem] = []
            for m in itemRx.matches(in: block, range: NSRange(location: 0, length: blockNS.length)) {
                if m.numberOfRanges == 4 {
                    let id = blockNS.substring(with: m.range(at: 1))
                    var img = blockNS.substring(with: m.range(at: 2))
                    let itemTitle = blockNS.substring(with: m.range(at: 3)).trimmingCharacters(in: .whitespacesAndNewlines)
                    if !img.hasPrefix("http") { img = base + img }
                    let optimized = optimizeImageUrl(img, width: 400, height: 600)
                    if !items.contains(where: { $0.id == id }) {
                        items.append(VideoItem(id: id, title: itemTitle, imageUrl: optimized, type: "post"))
                    }
                }
            }
            if !items.isEmpty { sections.append((name: title, items: items, tagId: tagId)) }
        }
        return (carouselItems, sections)
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
                if blockMatch.numberOfRanges >= 2, let blockRange = Range(blockMatch.range(at: 1), in: html) {
                    let block = String(html[blockRange])
                    func extract(_ pattern: String) -> String {
                        guard let rx = try? NSRegularExpression(pattern: pattern, options: []),
                              let m = rx.firstMatch(in: block, range: NSRange(block.startIndex..., in: block)),
                              m.numberOfRanges >= 2, let r = Range(m.range(at: 1), in: block)
                        else { return "" }
                        return String(block[r]).trimmingCharacters(in: .whitespacesAndNewlines)
                    }

                    let epId = extract(#"data-id="(\d+)""#)
                    guard !epId.isEmpty else { continue }
                    let epUrl = extract(#"data-url="([^"]*)""#)
                    if !epUrl.isEmpty {
                        let epTitle = extract(#"data-title="([^"]*)""#)
                        parsedEpisodes.append(EpisodeItem(
                            id: epId,
                            title: epTitle.isEmpty ? "الحلقة \(parsedEpisodes.count + 1)" : epTitle,
                            url: epUrl,
                            url720: extract(#"data-url720="([^"]*)""#),
                            url1080: extract(#"data-url1080="([^"]*)""#),
                            url360: extract(#"data-url360="([^"]*)""#),
                            url4k: extract(#"data-url4k="([^"]*)""#),
                            subtitleUrl: extract(#"data-srt="([^"]*)""#),
                            subtitleVttUrl: extract(#"data-webvtt="([^"]*)""#)
                        ))
                    }
                }
            }
        }

        if parsedEpisodes.isEmpty {
            d.isMovie = true
            let moviePattern = #"data-url="([^"]+)"[^>]*data-url360="([^"]*)"[^>]*(?:data-url4k="([^"]*)"[^>]*)?(?:data-url720="([^"]*)"[^>]*)?data-url1080="([^"]*)"[^>]*data-srt="([^"]*)"[^>]*data-webvtt="([^"]*)""#
            if let rx = try? NSRegularExpression(pattern: moviePattern, options: [.dotMatchesLineSeparators]),
               let m = rx.firstMatch(in: html, range: NSRange(html.startIndex..., in: html)) {
                if let r = Range(m.range(at: 1), in: html) { d.movieUrl = String(html[r]) }
                if let r = Range(m.range(at: 2), in: html) { d.movieUrl360 = String(html[r]) }
                if m.range(at: 3).location != NSNotFound, let r = Range(m.range(at: 3), in: html) { d.movieUrl4k = String(html[r]) }
                if m.range(at: 4).location != NSNotFound, let r = Range(m.range(at: 4), in: html) { d.movieUrl720 = String(html[r]) }
                if let r = Range(m.range(at: 5), in: html) { d.movieUrl1080 = String(html[r]) }
                if let r = Range(m.range(at: 6), in: html) { d.movieSubtitleUrl = String(html[r]) }
                if let r = Range(m.range(at: 7), in: html) { d.movieSubtitleVttUrl = String(html[r]) }
            }
        } else {
            d.isMovie = false
            d.episodes = parsedEpisodes
        }
        return d
    }
}

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
        self.init(.sRGB, red: Double(r) / 255, green: Double(g) / 255, blue: Double(b) / 255, opacity: Double(a) / 255)
    }
}
"""
with open("UTan/UTan/Scraper.swift", "w", encoding="utf-8") as f:
    f.write(scraper_swift)

# ==========================================
# 5. SubtitleParser.swift
# ==========================================
sub_parser_swift = r"""import Foundation

struct SubtitleCue: Identifiable {
    let id = UUID()
    let startTime: TimeInterval
    let endTime: TimeInterval
    let text: String
}

final class SubtitleParser {
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
        for block in content.components(separatedBy: "\n\n") {
            let lines = block.components(separatedBy: .newlines).map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }.filter { !$0.isEmpty }
            guard lines.count >= 3 else { continue }
            let text = lines[2...].joined(separator: "\n").replacingOccurrences(of: #"<[^>]+>"#, with: "", options: .regularExpression).trimmingCharacters(in: .whitespacesAndNewlines)
            if text.isEmpty { continue }
            let times = lines[1].components(separatedBy: " --> ")
            guard times.count == 2, let start = parseSRTTime(times[0]), let end = parseSRTTime(times[1]) else { continue }
            cues.append(SubtitleCue(startTime: start, endTime: end, text: text))
        }
        return cues
    }

    private static func parseSRTTime(_ timeString: String) -> TimeInterval? {
        let parts = timeString.trimmingCharacters(in: .whitespacesAndNewlines).components(separatedBy: ",")
        guard parts.count == 2, let milliseconds = Double(parts[1]) else { return nil }
        let tc = parts[0].components(separatedBy: ":")
        guard tc.count == 3, let h = Double(tc[0]), let m = Double(tc[1]), let s = Double(tc[2]) else { return nil }
        return h * 3600 + m * 60 + s + milliseconds / 1000
    }

    private static func parseWebVTT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let lines = content.components(separatedBy: .newlines)
        var i = 0
        while i < lines.count {
            let line = lines[i].trimmingCharacters(in: .whitespacesAndNewlines)
            if line.contains("-->") {
                let times = line.components(separatedBy: "-->")
                guard times.count == 2, let start = parseVTTTime(times[0]), let end = parseVTTTime(times[1]) else { i += 1; continue }
                var textLines: [String] = []
                i += 1
                while i < lines.count && !lines[i].trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
                    textLines.append(lines[i].trimmingCharacters(in: .whitespacesAndNewlines))
                    i += 1
                }
                let text = textLines.joined(separator: "\n").replacingOccurrences(of: #"<[^>]+>"#, with: "", options: .regularExpression).trimmingCharacters(in: .whitespacesAndNewlines)
                if !text.isEmpty { cues.append(SubtitleCue(startTime: start, endTime: end, text: text)) }
            }
            i += 1
        }
        return cues
    }

    private static func parseVTTTime(_ timeString: String) -> TimeInterval? {
        let parts = timeString.trimmingCharacters(in: .whitespacesAndNewlines).components(separatedBy: ":")
        var h: Double = 0, m: Double = 0, s: Double = 0
        if parts.count == 3 {
            h = Double(parts[0]) ?? 0
            m = Double(parts[1]) ?? 0
            let sp = parts[2].components(separatedBy: ".")
            s = (Double(sp[0]) ?? 0) + (sp.count == 2 ? (Double(sp[1]) ?? 0) / 1000 : 0)
        } else if parts.count == 2 {
            m = Double(parts[0]) ?? 0
            let sp = parts[1].components(separatedBy: ".")
            s = (Double(sp[0]) ?? 0) + (sp.count == 2 ? (Double(sp[1]) ?? 0) / 1000 : 0)
        } else { return nil }
        return h * 3600 + m * 60 + s
    }
}
"""
with open("UTan/UTan/SubtitleParser.swift", "w", encoding="utf-8") as f:
    f.write(sub_parser_swift)

# ==========================================
# 6. SupabaseManager.swift (كامل غير مقطوع)
# ==========================================
supabase_swift = r"""import Foundation
import Combine
import Security
import AuthenticationServices
import UIKit

enum SupabaseConfig {
    static let url     = "https://foygwdvggwmmzfbeoone.supabase.co"
    static let anonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZveWd3ZHZnZ3dtbXpmYmVvb25lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE5NjUzMjksImV4cCI6MjA5NzU0MTMyOX0.C8yY99ZUU841rTTQz-yyC1Hvz-hHu4sNKEFSsFTdgS0"
}

final class WebAuthPresentationContextProvider: NSObject, ASWebAuthenticationPresentationContextProviding {
    func presentationAnchor(for session: ASWebAuthenticationSession) -> ASPresentationAnchor {
        UIApplication.shared.connectedScenes
            .compactMap { ($0 as? UIWindowScene)?.windows.first(where: { $0.isKeyWindow }) }
            .first ?? ASPresentationAnchor()
    }
}

enum Keychain {
    static func set(_ value: String, for key: String) {
        let data = Data(value.utf8)
        let query: [String: Any] = [kSecClass as String: kSecClassGenericPassword, kSecAttrAccount as String: key]
        SecItemDelete(query as CFDictionary)
        var attrs = query
        attrs[kSecValueData as String] = data
        SecItemAdd(attrs as CFDictionary, nil)
    }
    static func get(_ key: String) -> String? {
        let query: [String: Any] = [kSecClass as String: kSecClassGenericPassword, kSecAttrAccount as String: key, kSecReturnData as String: true, kSecMatchLimit as String: kSecMatchLimitOne]
        var result: AnyObject?
        SecItemCopyMatching(query as CFDictionary, &result)
        guard let data = result as? Data else { return nil }
        return String(data: data, encoding: .utf8)
    }
    static func delete(_ key: String) {
        SecItemDelete([kSecClass as String: kSecClassGenericPassword, kSecAttrAccount as String: key] as CFDictionary)
    }
}

struct SupabaseUser: Codable {
    let id: String
    let email: String?
    let user_metadata: [String: AnyCodable]?
    var displayName: String {
        if let v = user_metadata?["display_name"]?.stringValue, !v.isEmpty { return v }
        return email?.components(separatedBy: "@").first ?? "مستخدم"
    }
}

struct AnyCodable: Codable {
    let value: Any
    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let v = try? container.decode(String.self) { value = v; return }
        if let v = try? container.decode(Bool.self) { value = v; return }
        if let v = try? container.decode(Double.self) { value = v; return }
        value = ""
    }
    func encode(to encoder: Encoder) throws {
        var container = encoder.singleValueContainer()
        if let v = value as? String { try container.encode(v) }
        else if let v = value as? Bool { try container.encode(v) }
        else if let v = value as? Double { try container.encode(v) }
        else { try container.encodeNil() }
    }
    var stringValue: String? { value as? String }
}

private struct AuthTokenResponse: Codable {
    let access_token: String
    let refresh_token: String
    let user: SupabaseUser
}

private struct AuthErrorResponse: Codable {
    let error_description: String?
    let msg: String?
    let message: String?
    var bestMessage: String? { error_description ?? msg ?? message }
}

struct CommentItem: Codable, Identifiable {
    let id: String
    let item_id: String
    let user_id: String
    let display_name: String
    let text: String
    let created_at: String
}

struct AuthTokenResponsePublic {
    let accessToken: String
    let refreshToken: String
    let user: SupabaseUser
}

enum AuthResult {
    case success
    case failure(String)
}

final class AuthSession: ObservableObject {
    static let shared = AuthSession()

    @Published private(set) var user: SupabaseUser?
    @Published private(set) var accessToken: String?
    @Published private(set) var isAdmin: Bool = false
    private var refreshToken: String?

    var isLoggedIn: Bool { user != nil && accessToken != nil }

    private init() {
        accessToken  = Keychain.get("ut_access_token")
        refreshToken = Keychain.get("ut_refresh_token")
        if let data = UserDefaults.standard.data(forKey: "ut_user"),
           let cached = try? JSONDecoder().decode(SupabaseUser.self, from: data) {
            user = cached
        }
        if user != nil && accessToken != nil {
            DispatchQueue.main.async {
                CloudSyncManager.shared.syncAfterLogin()
                SupabaseManager.shared.fetchIsAdmin { isAdmin in self.isAdmin = isAdmin }
            }
        }
    }

    func save(token: AuthTokenResponsePublic) {
        accessToken  = token.accessToken
        refreshToken = token.refreshToken
        user         = token.user
        Keychain.set(token.accessToken, for: "ut_access_token")
        Keychain.set(token.refreshToken, for: "ut_refresh_token")
        if let data = try? JSONEncoder().encode(token.user) { UserDefaults.standard.set(data, forKey: "ut_user") }
        CloudSyncManager.shared.syncAfterLogin()
        SupabaseManager.shared.fetchIsAdmin { [weak self] isAdmin in self?.isAdmin = isAdmin }
    }

    func signOut() {
        let tokenToRevoke = self.accessToken
        user = nil
        accessToken = nil
        refreshToken = nil
        isAdmin = false
        Keychain.delete("ut_access_token")
        Keychain.delete("ut_refresh_token")
        UserDefaults.standard.removeObject(forKey: "ut_user")
        if let token = tokenToRevoke { SupabaseManager.shared.logout(accessToken: token) { _ in } }
    }
}

final class CloudSyncManager {
    static let shared = CloudSyncManager()
    private init() {}
    func syncAfterLogin() {
        SupabaseManager.shared.fetchFavorites { favs in FavoritesStore.shared.mergeFromCloud(favs) }
        SupabaseManager.shared.fetchProgress { prog in WatchProgressStore.shared.mergeFromCloud(prog) }
    }
}

final class SupabaseManager {
    static let shared = SupabaseManager()
    private let session = URLSession.shared
    private var isConfigured: Bool { !SupabaseConfig.url.contains("YOUR-PROJECT-REF") }
    private var webAuthSession: ASWebAuthenticationSession?
    private let webAuthPresentationProvider = WebAuthPresentationContextProvider()

    func signUp(email: String, password: String, displayName: String, completion: @escaping (AuthResult) -> Void) {
        guard isConfigured, let url = URL(string: "\(SupabaseConfig.url)/auth/v1/signup") else { return }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.httpBody = try? JSONSerialization.data(withJSONObject: ["email": email, "password": password, "data": ["display_name": displayName]])
        performAuthRequest(req, completion: completion)
    }

    func signIn(email: String, password: String, completion: @escaping (AuthResult) -> Void) {
        guard isConfigured, let url = URL(string: "\(SupabaseConfig.url)/auth/v1/token?grant_type=password") else { return }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.httpBody = try? JSONSerialization.data(withJSONObject: ["email": email, "password": password])
        performAuthRequest(req, completion: completion)
    }

    func logout(accessToken: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let url = URL(string: "\(SupabaseConfig.url)/auth/v1/logout") else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(accessToken)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { _, _, _ in completion(true) }.resume()
    }

    func signInWithGoogle(completion: @escaping (AuthResult) -> Void) {
        guard isConfigured, var components = URLComponents(string: "\(SupabaseConfig.url)/auth/v1/authorize") else { return }
        components.queryItems = [URLQueryItem(name: "provider", value: "google"), URLQueryItem(name: "redirect_to", value: "utan://auth-callback")]
        guard let authUrl = components.url else { return }

        let s = ASWebAuthenticationSession(url: authUrl, callbackURLScheme: "utan") { [weak self] callbackUrl, error in
            if let error = error { completion(.failure(error.localizedDescription)); return }
            guard let callbackUrl = callbackUrl else { return }
            self?.handleOAuthCallback(url: callbackUrl, completion: completion)
        }
        s.presentationContextProvider = webAuthPresentationProvider
        s.prefersEphemeralWebBrowserSession = true
        self.webAuthSession = s
        s.start()
    }

    private func handleOAuthCallback(url: URL, completion: @escaping (AuthResult) -> Void) {
        let fragment = url.fragment ?? String(url.absoluteString.split(separator: "#").last ?? "")
        var params: [String: String] = [:]
        for pair in fragment.components(separatedBy: "&") {
            let kv = pair.components(separatedBy: "=")
            if kv.count == 2 { params[kv[0]] = kv[1].removingPercentEncoding ?? kv[1] }
        }
        guard let accessToken = params["access_token"], let refreshToken = params["refresh_token"] else { completion(.failure("فشل الدخول")); return }
        fetchUser(accessToken: accessToken) { user in
            guard let user = user else { completion(.failure("فشل جلب الحساب")); return }
            AuthSession.shared.save(token: AuthTokenResponsePublic(accessToken: accessToken, refreshToken: refreshToken, user: user))
            completion(.success)
        }
    }

    private func fetchUser(accessToken: String, completion: @escaping (SupabaseUser?) -> Void) {
        guard let url = URL(string: "\(SupabaseConfig.url)/auth/v1/user") else { completion(nil); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(accessToken)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data, let user = try? JSONDecoder().decode(SupabaseUser.self, from: data) else { completion(nil); return }
            DispatchQueue.main.async { completion(user) }
        }.resume()
    }

    private func performAuthRequest(_ request: URLRequest, completion: @escaping (AuthResult) -> Void) {
        session.dataTask(with: request) { data, response, error in
            DispatchQueue.main.async {
                if let error = error { completion(.failure(error.localizedDescription)); return }
                guard let data = data else { return }
                if let http = response as? HTTPURLResponse, !(200...299).contains(http.statusCode) {
                    let msg = (try? JSONDecoder().decode(AuthErrorResponse.self, from: data))?.bestMessage
                    completion(.failure(msg ?? "فشلت العملية")); return
                }
                guard let decoded = try? JSONDecoder().decode(AuthTokenResponse.self, from: data) else { return }
                AuthSession.shared.save(token: AuthTokenResponsePublic(accessToken: decoded.access_token, refreshToken: decoded.refresh_token, user: decoded.user))
                completion(.success)
            }
        }.resume()
    }

    func fetchIsAdmin(completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/admins?select=id") else { completion(false); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, response, _ in
            if let http = response as? HTTPURLResponse, http.statusCode == 200, let data = data, let arr = try? JSONSerialization.jsonObject(with: data) as? [Any], !arr.isEmpty {
                DispatchQueue.main.async { completion(true) }
            } else { DispatchQueue.main.async { completion(false) } }
        }.resume()
    }

    func fetchComments(itemId: String, completion: @escaping ([CommentItem]) -> Void) {
        guard isConfigured, var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/comments") else { completion([]); return }
        components.queryItems = [URLQueryItem(name: "item_id", value: "eq.\(itemId)"), URLQueryItem(name: "select", value: "*"), URLQueryItem(name: "order", value: "created_at.desc")]
        guard let url = components.url else { completion([]); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(AuthSession.shared.accessToken ?? SupabaseConfig.anonKey)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data, let items = try? JSONDecoder().decode([CommentItem].self, from: data) else { DispatchQueue.main.async { completion([]) }; return }
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    func postComment(itemId: String, text: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let user = AuthSession.shared.user, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/comments") else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("return=representation", forHTTPHeaderField: "Prefer")
        let body: [String: Any] = ["item_id": itemId, "user_id": user.id, "display_name": user.displayName, "text": text]
        req.httpBody = try? JSONSerialization.data(withJSONObject: body)
        session.dataTask(with: req) { _, response, _ in
            DispatchQueue.main.async { completion((response as? HTTPURLResponse)?.statusCode == 201) }
        }.resume()
    }

    func deleteComment(commentId: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/comments?id=eq.\(commentId)") else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "DELETE"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { _, response, _ in DispatchQueue.main.async { completion((200...299).contains((response as? HTTPURLResponse)?.statusCode ?? 0)) } }.resume()
    }

    func upsertFavorite(item: VideoItem, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let user = AuthSession.shared.user, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/favorites") else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("resolution=merge-duplicates", forHTTPHeaderField: "Prefer")
        let body: [String: Any] = ["item_id": item.id, "user_id": user.id, "title": item.title, "image_url": item.imageUrl, "type": item.type]
        req.httpBody = try? JSONSerialization.data(withJSONObject: body)
        session.dataTask(with: req) { _, response, _ in DispatchQueue.main.async { completion((200...299).contains((response as? HTTPURLResponse)?.statusCode ?? 0)) } }.resume()
    }

    func deleteFavorite(itemId: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/favorites?item_id=eq.\(itemId)") else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "DELETE"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { _, response, _ in DispatchQueue.main.async { completion((200...299).contains((response as? HTTPURLResponse)?.statusCode ?? 0)) } }.resume()
    }

    func fetchFavorites(completion: @escaping ([VideoItem]) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/favorites?select=*&order=created_at.desc") else { completion([]); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            struct FavRow: Codable { let item_id: String; let title: String; let image_url: String; let type: String }
            guard let data = data, let rows = try? JSONDecoder().decode([FavRow].self, from: data) else { DispatchQueue.main.async { completion([]) }; return }
            DispatchQueue.main.async { completion(rows.map { VideoItem(id: $0.item_id, title: $0.title, imageUrl: $0.image_url, type: $0.type) }) }
        }.resume()
    }

    func upsertProgress(_ prog: WatchProgress, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let user = AuthSession.shared.user, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/watch_progress") else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("resolution=merge-duplicates", forHTTPHeaderField: "Prefer")
        let body: [String: Any] = ["item_id": prog.itemId, "user_id": user.id, "title": prog.title, "image_url": prog.imageUrl, "episode_id": prog.episodeId, "episode_title": prog.episodeTitle, "progress_seconds": prog.progressSeconds, "duration_seconds": prog.durationSeconds, "updated_at": ISO8601DateFormatter().string(from: prog.updatedAt), "video_url": prog.videoUrl, "video_url720": prog.videoUrl720, "video_url1080": prog.videoUrl1080, "video_url360": prog.videoUrl360, "video_url4k": prog.videoUrl4k, "subtitle_url": prog.subtitleUrl, "subtitle_vtt_url": prog.subtitleVttUrl, "is_movie": prog.isMovie]
        req.httpBody = try? JSONSerialization.data(withJSONObject: body)
        session.dataTask(with: req) { _, response, _ in DispatchQueue.main.async { completion((200...299).contains((response as? HTTPURLResponse)?.statusCode ?? 0)) } }.resume()
    }

    func deleteProgress(itemId: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/watch_progress?item_id=eq.\(itemId)") else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "DELETE"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { _, response, _ in DispatchQueue.main.async { completion((200...299).contains((response as? HTTPURLResponse)?.statusCode ?? 0)) } }.resume()
    }

    func fetchProgress(completion: @escaping ([WatchProgress]) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let url = URL(string: "\(SupabaseConfig.url)/rest/v1/watch_progress?select=*") else { completion([]); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            struct ProgRow: Codable { let item_id: String; let title: String; let image_url: String; let episode_id: String; let episode_title: String; let progress_seconds: Double; let duration_seconds: Double; let updated_at: String; let video_url: String; let video_url720: String; let video_url1080: String; let video_url360: String; let video_url4k: String; let subtitle_url: String; let subtitle_vtt_url: String; let is_movie: Bool }
            guard let data = data, let rows = try? JSONDecoder().decode([ProgRow].self, from: data) else { DispatchQueue.main.async { completion([]) }; return }
            let fmt = ISO8601DateFormatter()
            DispatchQueue.main.async {
                completion(rows.map { WatchProgress(itemId: $0.item_id, title: $0.title, imageUrl: $0.image_url, episodeId: $0.episode_id, episodeTitle: $0.episode_title, progressSeconds: $0.progress_seconds, durationSeconds: $0.duration_seconds, updatedAt: fmt.date(from: $0.updated_at) ?? Date(), videoUrl: $0.video_url, videoUrl720: $0.video_url720, videoUrl1080: $0.video_url1080, videoUrl360: $0.video_url360, videoUrl4k: $0.video_url4k, subtitleUrl: $0.subtitle_url, subtitleVttUrl: $0.subtitle_vtt_url, isMovie: $0.is_movie) })
            }
        }.resume()
    }

    private func baseRequest(url: URL) -> URLRequest {
        var req = URLRequest(url: url)
        req.setValue(SupabaseConfig.anonKey, forHTTPHeaderField: "apikey")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        return req
    }
}
"""
with open("UTan/UTan/SupabaseManager.swift", "w", encoding="utf-8") as f:
    f.write(supabase_swift)

# ==========================================
# 7. Views.swift (تصميم سينمائي زجاجي فائق)
# ==========================================
views_swift = r"""import SwiftUI

// ─────────────────────────────────────────────
// MARK: – Main Tab View
// ─────────────────────────────────────────────
struct MainTabView: View {
    @EnvironmentObject var settings: AppSettings
    @State private var selection = 0

    var body: some View {
        TabView(selection: $selection) {
            HomeView()
                .tabItem { Label(L("الرئيسية", "Home"), systemImage: "house.fill") }
                .tag(0)
            BrowseView()
                .tabItem { Label(L("تصفح", "Browse"), systemImage: "square.grid.2x2.fill") }
                .tag(1)
            SearchView()
                .tabItem { Label(L("بحث", "Search"), systemImage: "magnifyingglass") }
                .tag(2)
            DownloadsView()
                .tabItem { Label(L("التنزيلات", "Downloads"), systemImage: "arrow.down.circle.fill") }
                .tag(3)
            AccountMainView()
                .tabItem { Label(L("حسابي", "Account"), systemImage: "person.crop.circle.fill") }
                .tag(4)
        }
        .tint(UT_RED)
        .preferredColorScheme(settings.appTheme == "amoled" ? .dark : .dark)
    }
}

// ─────────────────────────────────────────────
// MARK: – Home View
// ─────────────────────────────────────────────
struct HomeView: View {
    @EnvironmentObject var settings: AppSettings
    @StateObject private var scraper = MovieScraper()
    @StateObject private var progressStore = WatchProgressStore.shared
    @State private var isRefreshing = false

    var body: some View {
        NavigationStack {
            ZStack {
                APP_BG.ignoresSafeArea()

                ScrollView(.vertical, showsIndicators: false) {
                    VStack(spacing: 28) {
                        // الهيرو العُلوي
                        if !scraper.heroItems.isEmpty {
                            HeroCarousel(items: scraper.heroItems)
                                .frame(height: 480)
                        }

                        // المتابعة
                        if !progressStore.recent.isEmpty {
                            ContinueWatchingSection(items: progressStore.recent)
                        }

                        // الأقسام الحيوية
                        ForEach(scraper.categories, id: \.name) { cat in
                            if cat.tagId == -1 {
                                TopTenSection(title: cat.name, items: cat.items)
                            } else {
                                StandardSection(title: cat.name, items: cat.items, tagId: cat.tagId)
                            }
                        }
                    }
                    .padding(.bottom, 90)
                }
                .refreshable { scraper.refreshHome() }

                if scraper.isLoading && scraper.categories.isEmpty {
                    ProgressView()
                        .scaleEffect(1.5)
                        .tint(UT_RED)
                }
            }
            .navigationTitle("UTan")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    NavigationLink(destination: SettingsView()) {
                        Image(systemName: "gearshape.fill")
                            .foregroundColor(UT_WHITE)
                    }
                }
            }
        }
        .onAppear { if scraper.categories.isEmpty { scraper.fetchHome() } }
    }
}

// ─────────────────────────────────────────────
// MARK: – UI Components
// ─────────────────────────────────────────────
struct HeroCarousel: View {
    let items: [VideoItem]
    @EnvironmentObject var settings: AppSettings
    @State private var currentIndex = 0

    var body: some View {
        TabView(selection: $currentIndex) {
            ForEach(Array(items.enumerated()), id: \.element.id) { index, item in
                NavigationLink(destination: MediaDetailView(itemId: item.id)) {
                    ZStack(alignment: .bottom) {
                        CachedAsyncImage(url: URL(string: item.imageUrl)) { phase in
                            if let img = phase.image {
                                img.resizable().scaledToFill()
                            } else { Color.gray.opacity(0.2) }
                        }
                        .frame(height: 480)
                        .clipped()

                        // تدرج لوني سينمائي من الأسفل
                        LinearGradient(
                            gradient: Gradient(colors: [.clear, APP_BG.opacity(0.8), APP_BG]),
                            startPoint: .center, endPoint: .bottom
                        )

                        VStack(spacing: 12) {
                            Text(item.title)
                                .font(appFont(26, bold: true))
                                .foregroundColor(UT_WHITE)
                                .multilineTextAlignment(.center)
                                .lineLimit(2)
                                .padding(.horizontal)

                            HStack(spacing: 16) {
                                HStack {
                                    Image(systemName: "play.fill")
                                    Text(L("شاهد الآن", "Watch Now"))
                                        .font(appFont(16, bold: true))
                                }
                                .padding(.horizontal, 24)
                                .padding(.vertical, 12)
                                .background(UT_RED)
                                .foregroundColor(UT_WHITE)
                                .clipShape(Capsule())
                                .shadow(color: UT_RED.opacity(0.5), radius: 8, x: 0, y: 4)

                                Image(systemName: "info.circle")
                                    .font(.title2)
                                    .foregroundColor(UT_WHITE)
                                    .padding(10)
                                    .background(Material.ultraThin)
                                    .clipShape(Circle())
                            }
                        }
                        .padding(.bottom, 32)
                    }
                }
                .tag(index)
            }
        }
        .tabViewStyle(PageTabViewStyle(indexDisplayMode: .always))
    }
}

struct TopTenSection: View {
    let title: String
    let items: [VideoItem]
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            HStack(spacing: 8) {
                // استبدال الإيموجي بأيقونة احترافية
                Image(systemName: "flame.fill")
                    .foregroundColor(.orange)
                    .font(.title2)
                Text(title)
                    .font(appFont(22, bold: true))
                    .foregroundColor(UT_WHITE)
            }
            .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 16) {
                    ForEach(Array(items.enumerated()), id: \.element.id) { index, item in
                        NavigationLink(destination: MediaDetailView(itemId: item.id)) {
                            TopTenCard(item: item, rank: index + 1)
                        }
                    }
                }
                .padding(.horizontal)
            }
        }
    }
}

struct TopTenCard: View {
    let item: VideoItem
    let rank: Int
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        ZStack(alignment: .bottomLeading) {
            // البوستر بأسبيكت ريشيو دقيق
            CachedAsyncImage(url: URL(string: item.imageUrl)) { phase in
                if let img = phase.image {
                    img.resizable().scaledToFill()
                } else { Color.gray.opacity(0.2) }
            }
            .frame(width: 150, height: 225)
            .clipShape(RoundedRectangle(cornerRadius: 16))
            .shadow(color: .black.opacity(0.4), radius: 6, x: 0, y: 4)

            // حل مشكلة الترقيم: رقم ضخم فوق الصورة مع خلفية زجاجية شفافة
            Text("\(rank)")
                .font(utFont("expo", size: 60, bold: true))
                .foregroundColor(UT_WHITE)
                .padding(.horizontal, 8)
                .background(
                    LinearGradient(
                        colors: [APP_BG.opacity(0.9), .clear],
                        startPoint: .bottomLeading, endPoint: .topTrailing
                    )
                    .clipShape(RoundedRectangle(cornerRadius: 16))
                )
                .shadow(color: .black, radius: 4, x: 2, y: 2)
                .offset(x: -8, y: 15)
        }
        .frame(width: 160, height: 240)
    }
}

struct StandardSection: View {
    let title: String
    let items: [VideoItem]
    let tagId: Int
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack {
                Text(title)
                    .font(appFont(20, bold: true))
                    .foregroundColor(UT_WHITE)
                Spacer()
                NavigationLink(destination: CategoryListView(typeId: tagId, categoryName: title, isTag: true)) {
                    Text(L("المزيد", "More"))
                        .font(appFont(14, bold: true))
                        .foregroundColor(UT_RED)
                }
            }
            .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 14) {
                    ForEach(items) { item in
                        NavigationLink(destination: MediaDetailView(itemId: item.id)) {
                            VideoCard(item: item)
                        }
                    }
                }
                .padding(.horizontal)
            }
        }
    }
}

struct VideoCard: View {
    let item: VideoItem
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            CachedAsyncImage(url: URL(string: item.imageUrl)) { phase in
                if let img = phase.image {
                    img.resizable().scaledToFill()
                } else { Color.gray.opacity(0.2) }
            }
            .frame(width: 130, height: 195)
            .clipShape(RoundedRectangle(cornerRadius: 12))
            .shadow(color: .black.opacity(0.3), radius: 5, x: 0, y: 3)

            Text(item.title)
                .font(appFont(13, bold: true))
                .foregroundColor(UT_WHITE)
                .lineLimit(1)
                .frame(width: 130, alignment: .leading)
        }
    }
}

struct ContinueWatchingSection: View {
    let items: [WatchProgress]
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            Text(L("متابعة المشاهدة", "Continue Watching"))
                .font(appFont(20, bold: true))
                .foregroundColor(UT_WHITE)
                .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 16) {
                    ForEach(items) { prog in
                        NavigationLink(destination: MediaDetailView(itemId: prog.itemId)) {
                            ContinueCard(prog: prog)
                        }
                    }
                }
                .padding(.horizontal)
            }
        }
    }
}

struct ContinueCard: View {
    let prog: WatchProgress
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        ZStack(alignment: .bottom) {
            CachedAsyncImage(url: URL(string: prog.imageUrl)) { phase in
                if let img = phase.image { img.resizable().scaledToFill() }
                else { Color.gray.opacity(0.2) }
            }
            .frame(width: 220, height: 130)
            .clipShape(RoundedRectangle(cornerRadius: 14))

            Color.black.opacity(0.5)
                .frame(height: 50)
                .clipShape(RoundedRectangle(cornerRadius: 14))

            VStack(alignment: .leading, spacing: 4) {
                Text(prog.title)
                    .font(appFont(14, bold: true))
                    .foregroundColor(UT_WHITE)
                    .lineLimit(1)
                HStack {
                    Text(prog.episodeTitle)
                        .font(appFont(11, bold: false))
                        .foregroundColor(.gray)
                    Spacer()
                    Image(systemName: "play.circle.fill")
                        .foregroundColor(UT_RED)
                        .font(.title3)
                }
                ProgressView(value: prog.durationSeconds > 0 ? prog.progressSeconds / prog.durationSeconds : 0)
                    .tint(UT_RED)
            }
            .padding(8)
        }
        .frame(width: 220, height: 130)
        .shadow(color: .black.opacity(0.4), radius: 6, x: 0, y: 3)
    }
}

// ─────────────────────────────────────────────
// MARK: – Redesigned Media Detail View
// ─────────────────────────────────────────────
struct MediaDetailView: View {
    let itemId: String
    @EnvironmentObject var settings: AppSettings
    @StateObject private var scraper = MovieScraper()
    @StateObject private var favStore = FavoritesStore.shared
    @State private var details = MediaDetails()
    @State private var selectedTab = 0 // 0: الحلقات/التشغيل, 1: القصة, 2: التعليقات
    @State private var selectedSeason = "الموسم 1"
    @State private var activeEpisode: EpisodeItem?
    @State private var isPresentingPlayer = false

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()

            ScrollView(.vertical, showsIndicators: false) {
                VStack(spacing: 0) {
                    // الهيرو مع البانر المموّه
                    ZStack(alignment: .bottom) {
                        CachedAsyncImage(url: URL(string: details.imageUrl)) { phase in
                            if let img = phase.image { img.resizable().scaledToFill() }
                            else { Color.gray.opacity(0.2) }
                        }
                        .frame(height: 380)
                        .clipped()
                        .overlay(Material.ultraThin.opacity(0.4)) // تمويه سينمائي

                        LinearGradient(colors: [.clear, APP_BG], startPoint: .center, endPoint: .bottom)

                        HStack(alignment: .bottom, spacing: 20) {
                            CachedAsyncImage(url: URL(string: details.imageUrl)) { phase in
                                if let img = phase.image { img.resizable().scaledToFill() }
                                else { Color.gray }
                            }
                            .frame(width: 140, height: 210)
                            .clipShape(RoundedRectangle(cornerRadius: 16))
                            .shadow(color: .black.opacity(0.6), radius: 10, x: 0, y: 6)

                            VStack(alignment: .leading, spacing: 8) {
                                Text(details.title)
                                    .font(appFont(24, bold: true))
                                    .foregroundColor(UT_WHITE)
                                    .lineLimit(2)

                                HStack(spacing: 12) {
                                    if !details.rating.isEmpty {
                                        Label(details.rating, systemImage: "star.fill")
                                            .foregroundColor(.yellow)
                                            .font(appFont(14, bold: true))
                                    }
                                    Text(details.year)
                                        .foregroundColor(.gray)
                                        .font(appFont(14, bold: false))
                                }

                                Text(details.genre)
                                    .font(appFont(13, bold: false))
                                    .foregroundColor(.gray)
                                    .lineLimit(1)

                                // زر المفضلة
                                Button(action: {
                                    favStore.toggle(item: VideoItem(id: itemId, title: details.title, imageUrl: details.imageUrl, type: details.isMovie ? "movie" : "series"))
                                }) {
                                    Image(systemName: favStore.isFavorite(itemId) ? "heart.fill" : "heart")
                                        .foregroundColor(favStore.isFavorite(itemId) ? UT_RED : UT_WHITE)
                                        .font(.title2)
                                        .padding(10)
                                        .background(Material.ultraThin)
                                        .clipShape(Circle())
                                }
                            }
                            Spacer()
                        }
                        .padding(.horizontal)
                        .offset(y: 40)
                    }
                    .frame(height: 380)

                    // أزرار التحكم والتشغيل السريع
                    VStack(spacing: 24) {
                        if details.isMovie {
                            Button(action: {
                                activeEpisode = EpisodeItem(id: itemId, title: details.title, url: details.movieUrl, url720: details.movieUrl720, url1080: details.movieUrl1080, url360: details.movieUrl360, url4k: details.movieUrl4k, subtitleUrl: details.movieSubtitleUrl, subtitleVttUrl: details.movieSubtitleVttUrl)
                                isPresentingPlayer = true
                            }) {
                                HStack {
                                    Image(systemName: "play.fill")
                                    Text(L("تشغيل الفيلم", "Play Movie"))
                                        .font(appFont(18, bold: true))
                                }
                                .frame(maxWidth: .infinity)
                                .padding(.vertical, 16)
                                .background(UT_RED)
                                .foregroundColor(UT_WHITE)
                                .clipShape(RoundedRectangle(cornerRadius: 16))
                                .shadow(color: UT_RED.opacity(0.4), radius: 8, x: 0, y: 4)
                            }
                        }

                        // التبويبات الزجاجية
                        HStack(spacing: 0) {
                            DetailTabButton(title: details.isMovie ? L("التشغيل", "Play") : L("الحلقات", "Episodes"), isSelected: selectedTab == 0) { selectedTab = 0 }
                            DetailTabButton(title: L("القصة", "Synopsis"), isSelected: selectedTab == 1) { selectedTab = 1 }
                            DetailTabButton(title: L("التعليقات", "Comments"), isSelected: selectedTab == 2) { selectedTab = 2 }
                        }
                        .padding(4)
                        .background(Material.ultraThin)
                        .clipShape(RoundedRectangle(cornerRadius: 14))

                        // محتوى التبويبات
                        if selectedTab == 0 {
                            if !details.isMovie {
                                // اختيار الموسم
                                ScrollView(.horizontal, showsIndicators: false) {
                                    HStack(spacing: 12) {
                                        ForEach(details.sortedSeasons, id: \.self) { season in
                                            Button(action: { selectedSeason = season }) {
                                                Text(season)
                                                    .font(appFont(14, bold: true))
                                                    .padding(.horizontal, 16)
                                                    .padding(.vertical, 10)
                                                    .background(selectedSeason == season ? UT_RED : Color.clear)
                                                    .foregroundColor(selectedSeason == season ? UT_WHITE : .gray)
                                                    .clipShape(Capsule())
                                            }
                                        }
                                    }
                                }

                                // قائمة الحلقات
                                LazyVStack(spacing: 12) {
                                    ForEach(details.seasonsDict[selectedSeason] ?? [], id: \.id) { ep in
                                        EpisodeRow(ep: ep, details: details) {
                                            activeEpisode = ep
                                            isPresentingPlayer = true
                                        }
                                    }
                                }
                            }
                        } else if selectedTab == 1 {
                            Text(details.synopsis.isEmpty ? L("لا توجد قصة متاحة.", "No synopsis available.") : details.synopsis)
                                .font(appFont(16, bold: false))
                                .foregroundColor(UT_WHITE.opacity(0.9))
                                .lineSpacing(8)
                                .padding()
                                .background(Material.ultraThin)
                                .clipShape(RoundedRectangle(cornerRadius: 16))
                        } else {
                            CommentsSectionView(itemId: itemId)
                        }
                    }
                    .padding(.horizontal)
                    .padding(.top, 60)
                    .padding(.bottom, 90)
                }
            }
        }
        .onAppear { scraper.fetchDetails(id: itemId) { d in details = d; if let firstS = d.sortedSeasons.first { selectedSeason = firstS } } }
        .fullScreenCover(item: $activeEpisode) { ep in
            CustomPlayer(
                videoUrl: ep.url1080.isEmpty ? ep.url : ep.url1080,
                subtitleUrl: ep.subtitleUrl.isEmpty ? ep.subtitleVttUrl : ep.subtitleUrl,
                title: details.title,
                episodeTitle: details.isMovie ? "" : ep.title,
                itemId: itemId,
                episodeId: ep.id,
                imageUrl: details.imageUrl,
                isMovie: details.isMovie,
                mediaDetails: details
            )
        }
    }
}

struct DetailTabButton: View {
    let title: String
    let isSelected: Bool
    let action: () -> Void
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        Button(action: action) {
            Text(title)
                .font(appFont(15, bold: true))
                .foregroundColor(isSelected ? UT_WHITE : .gray)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 12)
                .background(isSelected ? UT_RED : Color.clear)
                .clipShape(RoundedRectangle(cornerRadius: 12))
        }
    }
}

struct EpisodeRow: View {
    let ep: EpisodeItem
    let details: MediaDetails
    let action: () -> Void
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        HStack(spacing: 16) {
            ZStack {
                Color.gray.opacity(0.2)
                Image(systemName: "play.fill")
                    .foregroundColor(UT_WHITE)
            }
            .frame(width: 50, height: 50)
            .clipShape(RoundedRectangle(cornerRadius: 12))

            VStack(alignment: .leading, spacing: 4) {
                Text(ep.title)
                    .font(appFont(15, bold: true))
                    .foregroundColor(UT_WHITE)
                HStack(spacing: 12) {
                    if !ep.url1080.isEmpty { Text("FHD").font(.system(size: 10, weight: .bold)).padding(4).background(Color.blue.opacity(0.3)).clipShape(RoundedRectangle(cornerRadius: 4)) }
                    if !ep.subtitleUrl.isEmpty || !ep.subtitleVttUrl.isEmpty { Text(L("مترجم", "Sub")).font(appFont(10, bold: true)).padding(4).background(Color.green.opacity(0.3)).clipShape(RoundedRectangle(cornerRadius: 4)) }
                }
            }
            Spacer()
            Button(action: { DownloadManager.shared.startDownload(item: VideoItem(id: ep.id, title: "\(details.title) - \(ep.title)", imageUrl: details.imageUrl, type: "series"), isMovie: false, vUrl: ep.url1080.isEmpty ? ep.url : ep.url1080, sUrl: ep.subtitleUrl.isEmpty ? ep.subtitleVttUrl : ep.subtitleUrl) }) {
                Image(systemName: "arrow.down.circle")
                    .foregroundColor(.gray)
                    .font(.title2)
            }
        }
        .padding(12)
        .background(Material.ultraThin)
        .clipShape(RoundedRectangle(cornerRadius: 14))
        .onTapGesture(perform: action)
    }
}

// ─────────────────────────────────────────────
// MARK: – Browse View
// ─────────────────────────────────────────────
struct BrowseView: View {
    @EnvironmentObject var settings: AppSettings
    @State private var selectedTab = 0 // 0: الكل, 1: أفلام, 2: مسلسلات, 3: أنمي

    let categories = SITE_CATEGORIES

    var filteredCategories: [SiteCategory] {
        switch selectedTab {
        case 1: return categories.filter { $0.nameAr.contains("أفلام") || $0.nameAr.contains("سينما") || $0.id == 0 }
        case 2: return categories.filter { $0.nameAr.contains("مسلسلات") || $0.id == 1 }
        case 3: return categories.filter { $0.nameAr.contains("أنمي") || $0.id == 2 }
        default: return categories
        }
    }

    let columns = [GridItem(.adaptive(minimum: 160), spacing: 16)]

    var body: some View {
        NavigationStack {
            ZStack {
                APP_BG.ignoresSafeArea()

                VStack(spacing: 16) {
                    // الفلاتر
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack(spacing: 12) {
                            FilterPill(title: L("الكل", "All"), isSelected: selectedTab == 0) { selectedTab = 0 }
                            FilterPill(title: L("أفلام", "Movies"), isSelected: selectedTab == 1) { selectedTab = 1 }
                            FilterPill(title: L("مسلسلات", "Series"), isSelected: selectedTab == 2) { selectedTab = 2 }
                            FilterPill(title: L("أنمي", "Anime"), isSelected: selectedTab == 3) { selectedTab = 3 }
                        }
                        .padding(.horizontal)
                    }

                    ScrollView(.vertical, showsIndicators: false) {
                        LazyVGrid(columns: columns, spacing: 16) {
                            ForEach(filteredCategories) { cat in
                                NavigationLink(destination: CategoryListView(typeId: cat.remoteId, categoryName: L(cat.nameAr, cat.nameEn), isTag: cat.isTag)) {
                                    CategoryCard(cat: cat)
                                }
                            }
                        }
                        .padding(.horizontal)
                        .padding(.bottom, 90)
                    }
                }
            }
            .navigationTitle(L("المكتبة", "Library"))
        }
    }
}

struct FilterPill: View {
    let title: String
    let isSelected: Bool
    let action: () -> Void
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        Button(action: action) {
            Text(title)
                .font(appFont(15, bold: true))
                .padding(.horizontal, 20)
                .padding(.vertical, 10)
                .background(isSelected ? UT_RED : Material.ultraThin)
                .foregroundColor(isSelected ? UT_WHITE : .gray)
                .clipShape(Capsule())
        }
    }
}

struct CategoryCard: View {
    let cat: SiteCategory
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        ZStack {
            LinearGradient(colors: [UT_SURFACE, UT_SURFACE.opacity(0.5)], startPoint: .topLeading, endPoint: .bottomTrailing)

            VStack(spacing: 12) {
                Image(systemName: iconFor(cat.id))
                    .font(.title)
                    .foregroundColor(UT_RED)
                Text(L(cat.nameAr, cat.nameEn))
                    .font(appFont(16, bold: true))
                    .foregroundColor(UT_WHITE)
                    .multilineTextAlignment(.center)
            }
            .padding()
        }
        .frame(height: 120)
        .clipShape(RoundedRectangle(cornerRadius: 16))
        .shadow(color: .black.opacity(0.2), radius: 6, x: 0, y: 3)
    }

    private func iconFor(_ id: Int) -> String {
        switch id {
        case 0, 7, 10, 18: return "film.fill"
        case 1, 4, 5, 15: return "tv.fill"
        case 2, 9: return "sparkles"
        default: return "folder.fill"
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Category List View (مع الترقيم المصلح)
// ─────────────────────────────────────────────
struct CategoryListView: View {
    let typeId: Int
    let categoryName: String
    let isTag: Bool
    @EnvironmentObject var settings: AppSettings
    @StateObject private var scraper = MovieScraper()
    @State private var items: [VideoItem] = []
    @State private var page = 1
    @State private var hasMore = true
    @State private var isLoading = false

    let columns = [GridItem(.adaptive(minimum: 110), spacing: 14)]

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()

            ScrollView(.vertical, showsIndicators: false) {
                LazyVGrid(columns: columns, spacing: 16) {
                    ForEach(items) { item in
                        NavigationLink(destination: MediaDetailView(itemId: item.id)) {
                            VideoCard(item: item)
                                .onAppear {
                                    if item == items.last && hasMore && !isLoading {
                                        loadMore()
                                    }
                                }
                        }
                    }
                }
                .padding()
                .padding(.bottom, 90)

                if isLoading {
                    ProgressView().tint(UT_RED).padding()
                }
            }
        }
        .navigationTitle(categoryName)
        .navigationBarTitleDisplayMode(.inline)
        .onAppear { if items.isEmpty { loadMore() } }
    }

    private func loadMore() {
        guard !isLoading else { return }
        isLoading = true
        scraper.fetchCategory(typeId: typeId, page: page, useTag: isTag) { newItems, more in
            items.append(contentsOf: newItems)
            hasMore = more
            page += 1
            isLoading = false
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Search View
// ─────────────────────────────────────────────
struct SearchView: View {
    @EnvironmentObject var settings: AppSettings
    @StateObject private var scraper = MovieScraper()
    @State private var query = ""
    @State private var results: [VideoItem] = []
    @State private var isSearching = false

    let columns = [GridItem(.adaptive(minimum: 110), spacing: 14)]

    var body: some View {
        NavigationStack {
            ZStack {
                APP_BG.ignoresSafeArea()

                VStack(spacing: 16) {
                    // شريط البحث
                    HStack {
                        Image(systemName: "magnifyingglass").foregroundColor(.gray)
                        TextField(L("ابحث عن فيلم، مسلسل، أنمي...", "Search movies, series..."), text: $query, onCommit: performSearch)
                            .font(appFont(16, bold: false))
                            .foregroundColor(UT_WHITE)
                        if !query.isEmpty {
                            Button(action: { query = ""; results.removeAll() }) {
                                Image(systemName: "xmark.circle.fill").foregroundColor(.gray)
                            }
                        }
                    }
                    .padding(14)
                    .background(Material.ultraThin)
                    .clipShape(RoundedRectangle(cornerRadius: 16))
                    .padding(.horizontal)

                    if isSearching {
                        Spacer()
                        ProgressView().tint(UT_RED).scaleEffect(1.5)
                        Spacer()
                    } else if results.isEmpty && !query.isEmpty {
                        Spacer()
                        Image(systemName: "film.stack").font(.system(size: 60)).foregroundColor(.gray.opacity(0.5))
                        Text(L("لا توجد نتائج مطابقة", "No results found")).font(appFont(18, bold: true)).foregroundColor(.gray)
                        Spacer()
                    } else {
                        ScrollView(.vertical, showsIndicators: false) {
                            LazyVGrid(columns: columns, spacing: 16) {
                                ForEach(results) { item in
                                    NavigationLink(destination: MediaDetailView(itemId: item.id)) {
                                        VideoCard(item: item)
                                    }
                                }
                            }
                            .padding()
                            .padding(.bottom, 90)
                        }
                    }
                }
            }
            .navigationTitle(L("البحث", "Search"))
        }
    }

    private func performSearch() {
        guard !query.isEmpty else { return }
        isSearching = true
        scraper.search(query: query) { res in
            results = res
            isSearching = false
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Downloads View
// ─────────────────────────────────────────────
struct DownloadsView: View {
    @EnvironmentObject var settings: AppSettings
    @StateObject private var dlManager = DownloadManager.shared

    var body: some View {
        NavigationStack {
            ZStack {
                APP_BG.ignoresSafeArea()

                if dlManager.activeDownloads.isEmpty {
                    VStack(spacing: 16) {
                        Image(systemName: "arrow.down.circle").font(.system(size: 70)).foregroundColor(.gray.opacity(0.4))
                        Text(L("قائمة التنزيلات فارغة", "No downloads yet")).font(appFont(20, bold: true)).foregroundColor(.gray)
                    }
                } else {
                    ScrollView(.vertical, showsIndicators: false) {
                        VStack(spacing: 16) {
                            ForEach(dlManager.activeDownloads) { item in
                                DownloadRow(item: item)
                            }
                        }
                        .padding()
                        .padding(.bottom, 90)
                    }
                }
            }
            .navigationTitle(L("التنزيلات", "Downloads"))
        }
    }
}

struct DownloadRow: View {
    let item: DownloadTaskItem
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        HStack(spacing: 16) {
            CachedAsyncImage(url: URL(string: item.imageUrl)) { phase in
                if let img = phase.image { img.resizable().scaledToFill() }
                else { Color.gray }
            }
            .frame(width: 60, height: 90)
            .clipShape(RoundedRectangle(cornerRadius: 10))

            VStack(alignment: .leading, spacing: 8) {
                Text(item.title).font(appFont(16, bold: true)).foregroundColor(UT_WHITE)
                if item.isCompleted {
                    Text(L("مكتمل", "Completed")).font(appFont(12, bold: true)).foregroundColor(.green)
                } else {
                    ProgressView(value: item.progress).tint(UT_RED)
                }
            }
            Spacer()
            Button(action: { DownloadManager.shared.cancel(id: item.id) }) {
                Image(systemName: "trash.fill").foregroundColor(.red).font(.title3)
            }
        }
        .padding(12)
        .background(Material.ultraThin)
        .clipShape(RoundedRectangle(cornerRadius: 14))
    }
}

// ─────────────────────────────────────────────
// MARK: – Settings View (تطبيق فوري للتعديلات)
// ─────────────────────────────────────────────
struct SettingsView: View {
    @EnvironmentObject var settings: AppSettings

    let fonts = ["Expo", "Cairo", "Rubik", "IBM", "System"]
    let themes = [("Dark", "dark"), ("AMOLED", "amoled"), ("Dark Blue", "dark_blue"), ("Dark Purple", "dark_purple")]
    let accents = [("Red", "red"), ("Blue", "blue"), ("Orange", "orange"), ("Green", "green"), ("Pink", "pink")]

    var body: some View {
        Form {
            Section(header: Text(L("المظهر واللغة", "Appearance & Language"))) {
                Picker(L("اللغة", "Language"), selection: $settings.appLanguage) {
                    Text("العربية").tag("ar")
                    Text("English").tag("en")
                }
                Picker(L("الثيم", "Theme"), selection: $settings.appTheme) {
                    ForEach(themes, id: \.1) { t in Text(t.0).tag(t.1) }
                }
                Picker(L("لون التطبيق", "Accent Color"), selection: $settings.accentColorName) {
                    ForEach(accents, id: \.1) { a in Text(a.0).tag(a.1) }
                }
            }

            Section(header: Text(L("خطوط وإعدادات الترجمة", "Subtitle Settings"))) {
                Picker(L("خط الترجمة", "Subtitle Font"), selection: $settings.subtitleFontName) {
                    ForEach(fonts, id: \.self) { f in Text(f).tag(f) }
                }
                Slider(value: $settings.subtitleFontSize, in: 16...36, step: 1) { Text(L("حجم الخط", "Font Size")) }
                ColorPicker(L("لون الترجمة", "Subtitle Color"), selection: Binding(get: { settings.subtitleColor }, set: { settings.subtitleColorHex = "#" + $0.description }))
            }

            Section(header: Text(L("التشغيل والتنزيل", "Playback & Download"))) {
                Toggle(L("التشغيل التلقائي للحلقة التالية", "Auto-play Next Episode"), isOn: $settings.autoPlayNextEnabled)
                Toggle(L("التنزيل عبر Wi-Fi فقط", "Download over Wi-Fi only"), isOn: $settings.downloadOverWifiOnly)
            }

            Section {
                Button(action: { settings.clearCache() }) {
                    Text(L("مسح الذاكرة المؤقتة", "Clear Cache")).foregroundColor(.red).font(appFont(16, bold: true))
                }
            }
        }
        .navigationTitle(L("الإعدادات", "Settings"))
    }
}

// ─────────────────────────────────────────────
// MARK: – Comments Section View
// ─────────────────────────────────────────────
struct CommentsSectionView: View {
    let itemId: String
    @EnvironmentObject var settings: AppSettings
    @State private var comments: [CommentItem] = []
    @State private var newComment = ""
    @State private var isPosting = false

    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            if AuthSession.shared.isLoggedIn {
                HStack {
                    TextField(L("أضف تعليقاً...", "Add a comment..."), text: $newComment)
                        .font(appFont(15, bold: false))
                        .padding(12)
                        .background(UT_SURFACE)
                        .clipShape(RoundedRectangle(cornerRadius: 12))
                        .foregroundColor(UT_WHITE)

                    Button(action: post) {
                        if isPosting { ProgressView().tint(UT_WHITE) }
                        else { Image(systemName: "paperplane.fill").foregroundColor(UT_WHITE) }
                    }
                    .padding(12)
                    .background(UT_RED)
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                    .disabled(newComment.isEmpty || isPosting)
                }
            } else {
                Text(L("قم بتسجيل الدخول لإضافة تعليق.", "Log in to post a comment."))
                    .font(appFont(14, bold: true))
                    .foregroundColor(.gray)
            }

            LazyVStack(spacing: 12) {
                ForEach(comments) { c in
                    VStack(alignment: .leading, spacing: 4) {
                        HStack {
                            Text(c.display_name).font(appFont(14, bold: true)).foregroundColor(UT_RED)
                            Spacer()
                            if AuthSession.shared.isAdmin || c.user_id == AuthSession.shared.user?.id {
                                Button(action: { SupabaseManager.shared.deleteComment(commentId: c.id) { _ in load() } }) {
                                    Image(systemName: "trash").foregroundColor(.red).font(.caption)
                                }
                            }
                        }
                        Text(c.text).font(appFont(15, bold: false)).foregroundColor(UT_WHITE)
                    }
                    .padding()
                    .background(Material.ultraThin)
                    .clipShape(RoundedRectangle(cornerRadius: 14))
                }
            }
        }
        .onAppear(perform: load)
    }

    private func load() { SupabaseManager.shared.fetchComments(itemId: itemId) { items in comments = items } }
    private func post() { guard !newComment.isEmpty else { return }; isPosting = true; SupabaseManager.shared.postComment(itemId: itemId, text: newComment) { success in if success { newComment = ""; load() }; isPosting = false } }
}
"""
with open("UTan/UTan/Views.swift", "w", encoding="utf-8") as f:
    f.write(views_swift)

# ==========================================
# 8. CustomPlayer.swift (مشغل سينمائي زجاجي)
# ==========================================
player_swift = r"""import SwiftUI
import AVKit
import AVFoundation

struct CustomPlayer: View {
    let videoUrl: String
    let subtitleUrl: String
    let title: String
    let episodeTitle: String
    let itemId: String
    let episodeId: String
    let imageUrl: String
    let isMovie: Bool
    let mediaDetails: MediaDetails

    @Environment(\.presentationMode) var presentationMode
    @EnvironmentObject var settings: AppSettings

    @StateObject private var playerViewModel = PlayerViewModel()
    @State private var showControls = true
    @State private var showSubtitleMenu = false
    @State private var autoPlayCountdown: Int?

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()

            PlayerView(player: playerViewModel.player)
                .ignoresSafeArea()
                .onTapGesture { withAnimation { showControls.toggle() } }

            // طبقة الترجمة
            if settings.subtitlesEnabled {
                VStack {
                    Spacer()
                    Text(playerViewModel.currentSubtitle ?? "")
                        .font(subtitleFontForPlayer(name: settings.subtitleFontName, size: CGFloat(settings.subtitleFontSize)))
                        .foregroundColor(settings.subtitleColor)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 24)
                        .padding(.vertical, 8)
                        .background(Color.black.opacity(playerViewModel.currentSubtitle?.isEmpty == false ? settings.subtitleBgOpacity : 0))
                        .clipShape(RoundedRectangle(cornerRadius: 10))
                        .padding(.bottom, CGFloat(settings.subtitleBottomPad))
                }
            }

            // واجهة التحكم الزجاجية
            if showControls {
                PlayerControlsView(
                    title: title,
                    episodeTitle: episodeTitle,
                    playerVM: playerViewModel,
                    showSubMenu: $showSubtitleMenu,
                    onBack: { saveProgressAndExit() }
                )
            }

            // العد التنازلي للحلقة التالية
            if let count = autoPlayCountdown {
                VStack(spacing: 16) {
                    Text(L("الحلقة القادمة تبدأ خلال", "Next episode starts in")).font(appFont(22, bold: true)).foregroundColor(UT_WHITE)
                    Text("\(count)").font(utFont("expo", size: 60, bold: true)).foregroundColor(UT_RED)
                    HStack(spacing: 20) {
                        Button(action: { playNextEpisode() }) { Text(L("تشغيل الآن", "Play Now")).font(appFont(16, bold: true)).padding(.horizontal, 24).padding(.vertical, 12).background(UT_RED).foregroundColor(UT_WHITE).clipShape(Capsule()) }
                        Button(action: { autoPlayCountdown = nil }) { Text(L("إلغاء", "Cancel")).font(appFont(16, bold: true)).padding(.horizontal, 24).padding(.vertical, 12).background(Material.ultraThin).foregroundColor(UT_WHITE).clipShape(Capsule()) }
                    }
                }
                .padding(32)
                .background(Material.ultraThin)
                .clipShape(RoundedRectangle(cornerRadius: 24))
            }
        }
        .onAppear { initPlayer() }
        .onDisappear { playerViewModel.player.pause() }
    }

    private func initPlayer() {
        guard let url = URL(string: videoUrl) else { return }
        let item = AVPlayerItem(url: url)
        playerViewModel.player.replaceCurrentItem(with: item)
        playerViewModel.player.play()
        SubtitleParser.parse(url: subtitleUrl) { cues in playerViewModel.subtitleCues = cues }

        // مراقبة انتهاء الفيديو للتشغيل التلقائي
        NotificationCenter.default.addObserver(forName: .AVPlayerItemDidPlayToEndTime, object: item, queue: .main) { _ in
            if !isMovie && settings.autoPlayNextEnabled && mediaDetails.nextEpisode(after: episodeId) != nil {
                startAutoPlayCountdown()
            }
        }
    }

    private func startAutoPlayCountdown() {
        autoPlayCountdown = settings.autoPlayCountdownSeconds
        Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { timer in
            guard let c = autoPlayCountdown else { timer.invalidate(); return }
            if c > 1 { autoPlayCountdown = c - 1 }
            else { timer.invalidate(); playNextEpisode() }
        }
    }

    private func playNextEpisode() {
        autoPlayCountdown = nil
        guard let nex = mediaDetails.nextEpisode(after: episodeId) else { return }
        saveProgressAndExit()
        // يمكن الربط مباشرة بتحديث الـ URL للمشغل الحالي
    }

    private func saveProgressAndExit() {
        if let item = playerViewModel.player.currentItem {
            let prog = item.currentTime().seconds
            let dur = item.duration.seconds
            if dur > 0 && prog > 5 {
                WatchProgressStore.shared.save(itemId: itemId, title: title, imageUrl: imageUrl, episodeId: episodeId, episodeTitle: episodeTitle, progress: prog, duration: dur, videoUrl: videoUrl, videoUrl720: "", videoUrl1080: "", videoUrl360: "", subUrl: subtitleUrl, subVttUrl: subtitleUrl, isMovie: isMovie)
            }
        }
        presentationMode.wrappedValue.dismiss()
    }
}

final class PlayerViewModel: ObservableObject {
    let player = AVPlayer()
    @Published var isPlaying = false
    @Published var duration: Double = 0
    @Published var currentTime: Double = 0
    @Published var currentSubtitle: String?
    var subtitleCues: [SubtitleCue] = []
    private var timeObserver: Any?

    init() {
        timeObserver = player.addPeriodicTimeObserver(forInterval: CMTime(seconds: 0.2, preferredTimescale: 600), queue: .main) { [weak self] time in
            guard let self = self else { return }
            self.currentTime = time.seconds
            if let dur = self.player.currentItem?.duration.seconds, !dur.isNaN { self.duration = dur }
            self.isPlaying = self.player.rate != 0

            // حساب الترجمة مع التقديم/التأخير
            let adjustedTime = time.seconds - AppSettings.shared.subtitleDelay
            self.currentSubtitle = self.subtitleCues.first(where: { adjustedTime >= $0.startTime && adjustedTime <= $0.endTime })?.text
        }
    }
    deinit { if let o = timeObserver { player.removeTimeObserver(o) } }
}

struct PlayerView: UIViewRepresentable {
    let player: AVPlayer
    func makeUIView(context: Context) -> UIView { let v = PlayerUIView(); v.player = player; return v }
    func updateUIView(_ uiView: UIView, context: Context) {}
}

final class PlayerUIView: UIView {
    var player: AVPlayer? { get { playerLayer.player } set { playerLayer.player = newValue } }
    var playerLayer: AVPlayerLayer { layer as! AVPlayerLayer }
    override static var layerClass: AnyClass { AVPlayerLayer.self }
}

struct PlayerControlsView: View {
    let title: String
    let episodeTitle: String
    @ObservedObject var playerVM: PlayerViewModel
    @Binding var showSubMenu: Bool
    let onBack: () -> Void
    @EnvironmentObject var settings: AppSettings

    var body: some View {
        VStack {
            // البار العُلوي الزجاجي
            HStack {
                Button(action: onBack) { Image(systemName: "chevron.left").font(.title2).foregroundColor(UT_WHITE).padding(12).background(Material.ultraThin).clipShape(Circle()) }
                VStack(alignment: .leading, spacing: 2) { Text(title).font(appFont(18, bold: true)).foregroundColor(UT_WHITE); if !episodeTitle.isEmpty { Text(episodeTitle).font(appFont(14, bold: false)).foregroundColor(.gray) } }
                Spacer()
                Button(action: { showSubMenu.toggle() }) { Image(systemName: "text.bubble.fill").font(.title2).foregroundColor(settings.subtitlesEnabled ? UT_RED : UT_WHITE).padding(12).background(Material.ultraThin).clipShape(Circle()) }
            }
            .padding(.horizontal, 24).padding(.top, 16)

            Spacer()

            // أزرار التحكم الوسطى
            HStack(spacing: 40) {
                Button(action: { seek(-15) }) { Image(systemName: "gobackward.15").font(.system(size: 36)).foregroundColor(UT_WHITE) }
                Button(action: { playerVM.isPlaying ? playerVM.player.pause() : playerVM.player.play() }) { Image(systemName: playerVM.isPlaying ? "pause.circle.fill" : "play.circle.fill").font(.system(size: 70)).foregroundColor(UT_RED) }
                Button(action: { seek(15) }) { Image(systemName: "goforward.15").font(.system(size: 36)).foregroundColor(UT_WHITE) }
            }

            Spacer()

            // شريط التقدم والبار السُفلي
            VStack(spacing: 8) {
                Slider(value: Binding(get: { playerVM.currentTime }, set: { playerVM.player.seek(to: CMTime(seconds: $0, preferredTimescale: 600)) }), in: 0...(playerVM.duration > 0 ? playerVM.duration : 1))
                    .tint(UT_RED)
                HStack { Text(format(playerVM.currentTime)).font(.caption.monospaced()).foregroundColor(.gray); Spacer(); Text(format(playerVM.duration)).font(.caption.monospaced()).foregroundColor(.gray) }
            }
            .padding(24).background(Material.ultraThin).clipShape(RoundedRectangle(cornerRadius: 24)).padding(.horizontal, 24).padding(.bottom, 24)
        }
        .sheet(isPresented: $showSubMenu) {
            NavigationView {
                Form {
                    Toggle(L("تفعيل الترجمة", "Enable Subtitles"), isOn: $settings.subtitlesEnabled)
                    Picker(L("الخط", "Font"), selection: $settings.subtitleFontName) { ForEach(["Expo", "Cairo", "Rubik", "IBM", "System"], id: \.self) { Text($0).tag($0) } }
                    Stepper(value: $settings.subtitleDelay, step: 0.5) { Text(L("تأخير الترجمة: \(settings.subtitleDelay, specifier: "%.1f")ث", "Sub Delay: \(settings.subtitleDelay, specifier: "%.1f")s")) }
                }
                .navigationTitle(L("إعدادات الترجمة", "Subtitles"))
                .navigationBarItems(trailing: Button("OK") { showSubMenu = false })
            }
            .presentationDetents([.medium])
        }
    }

    private func seek(_ sec: Double) { if let t = playerVM.player.currentItem?.currentTime() { playerVM.player.seek(to: CMTime(seconds: t.seconds + sec, preferredTimescale: 600)) } }
    private func format(_ sec: Double) -> String { let s = Int(sec); let m = s / 60; let h = m / 60; return h > 0 ? String(format: "%d:%02d:%02d", h, m % 60, s % 60) : String(format: "%02d:%02d", m, s % 60) }
}
"""
with open("UTan/UTan/CustomPlayer.swift", "w", encoding="utf-8") as f:
    f.write(player_swift)

# ==========================================
# 9. AccountViews.swift (حساب زجاجي أنيق)
# ==========================================
account_swift = r"""import SwiftUI

struct AccountMainView: View {
    @EnvironmentObject var settings: AppSettings
    @StateObject private var auth = AuthSession.shared

    var body: some View {
        NavigationStack {
            ZStack {
                APP_BG.ignoresSafeArea()
                if auth.isLoggedIn { ProfileView() }
                else { AuthEntryView() }
            }
            .navigationTitle(L("حسابي", "My Account"))
        }
    }
}

struct AuthEntryView: View {
    @EnvironmentObject var settings: AppSettings
    @State private var email = ""
    @State private var password = ""
    @State private var isSignUp = false
    @State private var displayName = ""
    @State private var isLoading = false
    @State private var errMsg: String?

    var body: some View {
        VStack(spacing: 24) {
            Image("logo").resizable().scaledToFit().frame(width: 120)
            Text(isSignUp ? L("إنشاء حساب جديد", "Create Account") : L("تسجيل الدخول", "Welcome Back")).font(appFont(26, bold: true)).foregroundColor(UT_WHITE)

            VStack(spacing: 16) {
                if isSignUp { TextField(L("الاسم", "Name"), text: $displayName).padding(16).background(UT_SURFACE).clipShape(RoundedRectangle(cornerRadius: 16)).foregroundColor(UT_WHITE) }
                TextField(L("البريد الإلكتروني", "Email"), text: $email).autocapitalization(.none).padding(16).background(UT_SURFACE).clipShape(RoundedRectangle(cornerRadius: 16)).foregroundColor(UT_WHITE)
                SecureField(L("كلمة المرور", "Password"), text: $password).padding(16).background(UT_SURFACE).clipShape(RoundedRectangle(cornerRadius: 16)).foregroundColor(UT_WHITE)
            }
            .padding(.horizontal)

            if let err = errMsg { Text(err).foregroundColor(.red).font(appFont(14, bold: true)) }

            Button(action: submit) {
                if isLoading { ProgressView().tint(UT_WHITE) }
                else { Text(isSignUp ? L("تسجيل", "Sign Up") : L("دخول", "Log In")).font(appFont(18, bold: true)).frame(maxWidth: .infinity).padding(.vertical, 16).background(UT_RED).foregroundColor(UT_WHITE).clipShape(RoundedRectangle(cornerRadius: 16)) }
            }
            .padding(.horizontal)

            Button(action: { SupabaseManager.shared.signInWithGoogle { _ in } }) {
                HStack { Image(systemName: "g.circle.fill").font(.title2); Text(L("الدخول بواسطة Google", "Continue with Google")).font(appFont(16, bold: true)) }
                .frame(maxWidth: .infinity).padding(.vertical, 14).background(Material.ultraThin).foregroundColor(UT_WHITE).clipShape(RoundedRectangle(cornerRadius: 16))
            }
            .padding(.horizontal)

            Button(action: { isSignUp.toggle(); errMsg = nil }) { Text(isSignUp ? L("لديك حساب؟ سجل دخولك", "Already have an account? Log in") : L("ليس لديك حساب؟ سجل الآن", "Don't have an account? Sign up")).font(appFont(14, bold: true)).foregroundColor(UT_RED) }
        }
    }

    private func submit() {
        isLoading = true; errMsg = nil
        let cb: (AuthResult) -> Void = { res in isLoading = false; if case .failure(let err) = res { errMsg = err } }
        if isSignUp { SupabaseManager.shared.signUp(email: email, password: password, displayName: displayName.isEmpty ? "مستخدم" : displayName, completion: cb) }
        else { SupabaseManager.shared.signIn(email: email, password: password, completion: cb) }
    }
}

struct ProfileView: View {
    @EnvironmentObject var settings: AppSettings
    @StateObject private var auth = AuthSession.shared
    @StateObject private var favStore = FavoritesStore.shared

    let columns = [GridItem(.adaptive(minimum: 110), spacing: 14)]

    var body: some View {
        ScrollView(.vertical, showsIndicators: false) {
            VStack(spacing: 24) {
                VStack(spacing: 12) {
                    Image(systemName: "person.crop.circle.fill").font(.system(size: 80)).foregroundColor(UT_RED)
                    Text(auth.user?.displayName ?? "مستخدم").font(appFont(22, bold: true)).foregroundColor(UT_WHITE)
                    Text(auth.user?.email ?? "").font(appFont(14, bold: false)).foregroundColor(.gray)
                }
                .padding().frame(maxWidth: .infinity).background(Material.ultraThin).clipShape(RoundedRectangle(cornerRadius: 24)).padding(.horizontal)

                VStack(alignment: .leading, spacing: 14) {
                    Text(L("قائمة المفضلة", "My Favorites")).font(appFont(20, bold: true)).foregroundColor(UT_WHITE).padding(.horizontal)
                    if favStore.items.isEmpty { Text(L("لا توجد عناصر في المفضلة.", "No favorites yet.")).foregroundColor(.gray).padding(.horizontal) }
                    else { LazyVGrid(columns: columns, spacing: 16) { ForEach(favStore.items) { item in NavigationLink(destination: MediaDetailView(itemId: item.id)) { VideoCard(item: item) } } }.padding(.horizontal) }
                }

                Button(action: { auth.signOut() }) { Text(L("تسجيل الخروج", "Log Out")).font(appFont(18, bold: true)).frame(maxWidth: .infinity).padding(.vertical, 16).background(Color.red.opacity(0.2)).foregroundColor(.red).clipShape(RoundedRectangle(cornerRadius: 16)) }.padding(.horizontal)
            }
            .padding(.bottom, 90)
        }
    }
}
"""
with open("UTan/UTan/AccountViews.swift", "w", encoding="utf-8") as f:
    f.write(account_swift)

print("✅ تم بناء كامل بنية المشروع وملفاته البرمجية بنجاح واحترافية مطلقة!")
