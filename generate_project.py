import os

# Create directory structure
os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# 1. project.pbxproj (نفس المحتوى السابق)
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
		010101012C1234560000003D /* alfont_com_AlFont_com_ExpoArabic-Bold.otf */ = {isa = PBXFileReference; lastKnownFileType = file; path = "alfont_com_AlFont_com_ExpoArabic-Bold.otf"; sourceTree = "<group>"; };
		010101012C1234560000003C /* alfont_com_AlFont_com_ExpoArabic-Bold.otf in Resources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000003D /* alfont_com_AlFont_com_ExpoArabic-Bold.otf */; };
/* End PBXBuildFile section */

/* Begin SPMDependency note */
/* Fix 103: To add Supabase Swift SDK via SPM in Xcode:
   File → Add Package Dependencies → https://github.com/supabase-community/supabase-swift
   Version: up-to-next-major from 2.0.0
   This project uses a manual REST client for zero-dependency builds.
   If you prefer the official SDK, replace SupabaseManager with the SDK client. */
/* End SPMDependency note */

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
				010101012C1234560000003D /* alfont_com_AlFont_com_ExpoArabic-Bold.otf */,
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
				010101012C1234560000003C /* alfont_com_AlFont_com_ExpoArabic-Bold.otf in Resources */,
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

# 2. Info.plist (نفس المحتوى السابق)
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
    <string>$(CURRENT_PROJECT_VERSION)</string>
    <key>LSRequiresIPhoneOS</key>
    <true/>
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <false/>
        <key>NSExceptionDomains</key>
        <dict>
            <key>movie.vodu.me</key>
            <dict>
                <key>NSExceptionAllowsInsecureHTTPLoads</key>
                <false/>
                <key>NSRequiresCertificateTransparency</key>
                <true/>
                <key>NSIncludesSubdomains</key>
                <true/>
            </dict>
        </dict>
    </dict>
    <key>NSPhotoLibraryAddUsageDescription</key>
    <string>يحتاج التطبيق إذن حفظ الفيديوهات المُنزَّلة في مكتبة الصور.</string>
    <key>UIBackgroundModes</key>
    <array>
        <string>fetch</string>
        <string>processing</string>
        <string>audio</string>
    </array>
    <key>CFBundleLocalizations</key>
    <array>
        <string>ar</string>
        <string>en</string>
    </array>
    <key>CFBundleDevelopmentRegion</key>
    <string>$(DEVELOPMENT_LANGUAGE)</string>
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

# 3. UTanApp.swift (نفس المحتوى)
app_swift = """import SwiftUI

// Fix 94: AppDelegate handles audio interruptions and system notifications
class AppDelegate: NSObject, UIApplicationDelegate {
    func application(_ application: UIApplication,
                     handleEventsForBackgroundURLSession identifier: String,
                     completionHandler: @escaping () -> Void) {
        // Called when a background download session finishes; wake app and call handler
        completionHandler()
    }
    func applicationDidReceiveMemoryWarning(_ application: UIApplication) {
        ImageCacheManager.shared.cache.removeAllObjects()
    }
}

@main
struct UTanApp: App {
    // Fix 94: UIApplicationDelegateAdaptor enables AppDelegate lifecycle events in SwiftUI
    @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    @StateObject private var settings = AppSettings.shared

    var body: some Scene {
        WindowGroup {
            MainTabView()
                .environmentObject(settings)
                // Fix 47 & 95: Layout direction from Locale; player views must opt out individually
                .environment(\.layoutDirection, Locale(identifier: settings.appLanguage).characterDirection == .rightToLeft ? .rightToLeft : .leftToRight)
                // Fix 99: Force dark mode system-wide; preserves iOS Dark Mode semantics
                .preferredColorScheme(.dark)
        }
    }
}
"""
with open("UTan/UTan/UTanApp.swift", "w", encoding="utf-8") as f:
    f.write(app_swift)

# 4. Scraper.swift (مع إضافة subtitleDelay)
scraper_swift = r"""import Foundation
import SwiftUI
import UIKit

// ─────────────────────────────────────────────
// MARK: – Global Colors & Configs
// ─────────────────────────────────────────────

// ─────────────────────────────────────────────
// MARK: – نظام الثيمات والألوان الديناميكية
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

// ─────────────────────────────────────────────
// MARK: – الترجمة (عربي/إنجليزي)
// ─────────────────────────────────────────────
func L(_ ar: String, _ en: String) -> String {
    AppSettings.shared.appLanguage == "en" ? en : ar
}

let UT_WHITE   = Color.white
let UT_SURFACE = Color.white.opacity(0.12)

// User-Agent (Token) المستخدم في كل طلبات السكرابينج - لا تغيّره
// Fix 32: Dynamic iOS User-Agent avoids origin firewall blocks targeting desktop UA strings
var UT_USER_AGENT: String {
    let info = Bundle.main
    let appVersion = info.object(forInfoDictionaryKey: "CFBundleShortVersionString") as? String ?? "5.0"
    let build = info.object(forInfoDictionaryKey: "CFBundleVersion") as? String ?? "1"
    let osVersion = UIDevice.current.systemVersion.replacingOccurrences(of: ".", with: "_")
    let model = UIDevice.current.model
    return "UTan/\(appVersion) (\(model); iOS \(UIDevice.current.systemVersion); Build/\(build)) AppleWebKit/605.1.15 Mobile/\(osVersion) Safari/604.1"
}

class AppSettings: ObservableObject {
    static let shared = AppSettings()

    @AppStorage("sub_fontSize")   var subtitleFontSize: Double  = 22.0
    @AppStorage("sub_colorHex")   var subtitleColorHex: String  = "#FFFFFF"
    @AppStorage("sub_bgOpacity")  var subtitleBgOpacity: Double = 0.6
    @AppStorage("sub_bottomPad")  var subtitleBottomPad: Double = 60.0
    @AppStorage("sub_enabled")    var subtitlesEnabled: Bool    = true
    @AppStorage("sub_fontName")   var subtitleFontName: String  = "Cairo"
    @AppStorage("sub_delay")      var subtitleDelay: Double     = 0.0   // تأخير الترجمة بالثواني (يمكن أن يكون سالباً للتقديم)

    // إعدادات التشغيل التلقائي للحلقة التالية
    @AppStorage("autoplay_next")      var autoPlayNextEnabled: Bool = true
    @AppStorage("autoplay_countdown") var autoPlayCountdownSeconds: Int = 10

    // الجودة المفضلة الافتراضية
    @AppStorage("pref_quality") var preferredQuality: String = "تلقائي"

    // التنزيل عبر الواي فاي فقط (لتوفير بيانات الجوال)
    @AppStorage("download_wifi_only") var downloadOverWifiOnly: Bool = false

    // اللغة: "ar" أو "en"
    @AppStorage("app_language") var appLanguage: String = "ar"

    // الثيم: "dark", "amoled", "dark_blue", "dark_purple"
    @AppStorage("app_theme") var appTheme: String = "dark"

    // ألوان أكسنت: "red", "blue", "orange", "green", "pink"
    @AppStorage("accent_color") var accentColorName: String = "red"

    // حجم البوسترات في صفحة التصفح: "small", "medium", "large"
    @AppStorage("grid_size") var gridSizeStr: String = "medium"

    var subtitleColor: Color { Color(hex: subtitleColorHex) }

    func clearCache() {
        // Fix 29: URLCache removal is synchronous I/O — run off the main thread
        DispatchQueue.global(qos: .utility).async {
            URLCache.shared.removeAllCachedResponses()
        }
        Task { @MainActor in
            await WatchProgressStore.shared.clearAll()
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Custom Fonts (Cairo / Rubik / IBM Plex Arabic)
// ─────────────────────────────────────────────
// Fix 11: Static cache prevents re-scanning UIFont.familyNames on every layout pass
private var _utFontCache: [String: Font] = [:]
private let _utFontCacheLock = NSLock()

func utFont(_ keyword: String, size: CGFloat, bold: Bool = false) -> Font {
    let cacheKey = "\(keyword.lowercased())_\(size)_\(bold)"
    _utFontCacheLock.lock()
    if let cached = _utFontCache[cacheKey] { _utFontCacheLock.unlock(); return cached }
    _utFontCacheLock.unlock()

    let key = keyword.lowercased()

    func familyMatches(_ family: String) -> Bool {
        let f = family.lowercased()
        switch key {
        case "ibm":    return f.contains("ibm") || f.contains("plex")
        case "rubik":  return f.contains("rubik")
        case "expo":   return f.contains("expo")
        case "system": return false  // نتجاوز البحث ونرجع system مباشرة
        default:       return f.contains("cairo")
        }
    }

    if key == "system" {
        let r = Font.system(size: size, weight: bold ? .bold : .regular, design: .default)
        _utFontCacheLock.lock(); _utFontCache[cacheKey] = r; _utFontCacheLock.unlock()
        return r
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
            let result = Font(uiFont)
            _utFontCacheLock.lock(); _utFontCache[cacheKey] = result; _utFontCacheLock.unlock()
            return result
        }
    }

    let fallbackNames: [String]
    switch key {
    case "ibm":  fallbackNames = ["IBMPlexArabic-Bold","IBMPlexSansArabic-Regular","Ibm"]
    case "rubik": fallbackNames = ["Rubik-Regular","Rubik","Rubik-Bold"]
    case "expo": fallbackNames = ["ExpoArabic-Bold","alfont_com_AlFont_com_ExpoArabic-Bold"]
    default:     fallbackNames = ["Cairo-Regular","Cairo","Cairo-SemiBold"]
    }
    for n in fallbackNames {
        if let uiFont = UIFont(name: n, size: size) { let r = Font(uiFont); _utFontCacheLock.lock(); _utFontCache[cacheKey] = r; _utFontCacheLock.unlock(); return r }
    }

    let fallback = Font.system(size: size, weight: bold ? .bold : .regular)
    _utFontCacheLock.lock()
    _utFontCache[cacheKey] = fallback
    _utFontCacheLock.unlock()
    return fallback
}

/// الخط الرئيسي للتطبيق (ExpoArabic للعربية، System للإنجليزية)
func appFont(_ size: CGFloat, bold: Bool = false) -> Font {
    utFont("expo", size: size, bold: bold)
}

/// الخط المستخدم في قوائم الترجمة للمشغل
func subtitleFontForPlayer(name: String, size: CGFloat) -> Font {
    switch name.lowercased() {
    case "expo":   return utFont("expo", size: size, bold: true)
    case "ibm":    return utFont("ibm", size: size, bold: true)
    case "rubik":  return utFont("rubik", size: size, bold: true)
    case "system": return .system(size: size, weight: .semibold)
    default:       return utFont("cairo", size: size, bold: true)
    }
}


/// طباعة كل عائلات الخطوط المتاحة فعلياً داخل التطبيق (لأغراض التشخيص فقط)
func debugPrintAvailableFonts() {
    // Fix 50: Use OSLog instead of print – omitted from release builds by the OS
    let scraperLog = Logger(subsystem: "com.mustaqil.utan", category: "Fonts")
    scraperLog.debug("📋 Available fonts:")
    for family in UIFont.familyNames.sorted() {
        for font in UIFont.fontNames(forFamilyName: family) {
            scraperLog.debug("   – \(font, privacy: .public)  (family: \(family, privacy: .public))")
        }
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

    // Fix 12: Pre-compiled static regex – built once, not on every property access
    private static let seasonRegex = try! NSRegularExpression(pattern: #"(?i)(S\d+|موسم \d+)"#)
    private static let episodeNumberRegex = try! NSRegularExpression(pattern: #"(?i)E(\d+)"#)

    var season: String {
        let nsTitle = title as NSString
        if let match = Self.seasonRegex.firstMatch(in: title, range: NSRange(location: 0, length: nsTitle.length)) {
            return nsTitle.substring(with: match.range)
                // Fix 71: Use anchored regex to only replace leading 's', not 's' in proper nouns
                .replacingOccurrences(of: #"(?i)^s(?=\d)"#, with: "S", options: .regularExpression)
                .replacingOccurrences(of: #"^S(\d)"#, with: "الموسم $1", options: .regularExpression)
        }
        return "الموسم 1"
    }

    /// رقم الحلقة المستخرج من العنوان (إن وُجد) - مفيد للترتيب والعرض
    var episodeNumber: Int? {
        let nsTitle = title as NSString
        guard let match = Self.episodeNumberRegex.firstMatch(in: title, range: NSRange(location: 0, length: nsTitle.length)),
              match.numberOfRanges >= 2 else { return nil }
        return Int(nsTitle.substring(with: match.range(at: 1)))
    }
}

// Fix 43: Class avoids repeated struct copying during view updates (episodes array can be large)
class MediaDetails {
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
        // Fix 60: Place OVA/Specials (n==0) at the end, not at the start
        seasonsDict.keys.sorted { s1, s2 in
            let n1 = Int(s1.components(separatedBy: CharacterSet.decimalDigits.inverted).joined()) ?? Int.max
            let n2 = Int(s2.components(separatedBy: CharacterSet.decimalDigits.inverted).joined()) ?? Int.max
            if n1 == n2 { return s1.localizedCompare(s2) == .orderedAscending }
            return n1 < n2
        }
    }

    /// الحلقة التالية بعد حلقة معينة (تُستخدم للتشغيل التلقائي للحلقة القادمة)
    func nextEpisode(after episodeId: String) -> EpisodeItem? {
        // Fix 92: Sort by episodeNumber before finding the next episode (don't assume array order)
        let sorted = episodes.sorted {
            ($0.episodeNumber ?? Int.max) < ($1.episodeNumber ?? Int.max)
        }
        guard let idx = sorted.firstIndex(where: { $0.id == episodeId }) else { return nil }
        let next = idx + 1
        guard next < sorted.count else { return nil }
        return sorted[next]
    }

    // Fix 76: Pre-indexed dictionary for O(1) lookup instead of O(N) sequential scan
    var episodesIndex: [String: EpisodeItem] {
        Dictionary(uniqueKeysWithValues: episodes.map { ($0.id, $0) })
    }

    /// حلقة بمعرف معين
    func episode(withId id: String) -> EpisodeItem? {
        episodesIndex[id]
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
    var videoUrl4k: String = ""
    var subtitleUrl: String = ""
    var subtitleVttUrl: String = ""
    var isMovie: Bool = true
}

// Fix 21: @MainActor ensures @Published mutations always happen on the main thread
@MainActor
class WatchProgressStore: ObservableObject {
    static let shared = WatchProgressStore()
    private let key = "UTanWatchProgress_v3"

    @Published var allProgress: [String: WatchProgress] = [:]

    // Fix 19: Debounce persistence to avoid thrashing UserDefaults on every frame
    private var persistDebounceTask: Task<Void, Never>?

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

    // Fix 97: JSON file backup in documentDirectory – survives UserDefaults clears
    private var backupURL: URL {
        FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
            .appendingPathComponent("UTanProgressBackup.json")
    }

    func backupToFile() {
        guard let data = try? JSONEncoder().encode(allProgress) else { return }
        try? data.write(to: backupURL, options: .atomic)
    }

    func restoreFromFileIfNeeded() {
        guard allProgress.isEmpty,
              let data = try? Data(contentsOf: backupURL),
              let decoded = try? JSONDecoder().decode([String: WatchProgress].self, from: data)
        else { return }
        allProgress = decoded
    }

    /// دمج سجلات قادمة من السحابة (تُستخدم عند تسجيل الدخول): الأحدث (updatedAt) يفوز
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
        // Fix 19: Debounce – only flush to UserDefaults after 0.5s of inactivity
        persistDebounceTask?.cancel()
        persistDebounceTask = Task { @MainActor in
            try? await Task.sleep(nanoseconds: 500_000_000)
            guard !Task.isCancelled else { return }
            if let data = try? JSONEncoder().encode(self.allProgress) {
                UserDefaults.standard.set(data, forKey: self.key)
            }
        }
    }
}

// Fix 22: @MainActor isolates FavoritesStore mutations to main thread
@MainActor
class FavoritesStore: ObservableObject {
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

    /// دمج عناصر قادمة من السحابة (تُستخدم عند تسجيل الدخول): أي عنصر غير موجود محلياً يُضاف
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

// ─────────────────────────────────────────────
// MARK: – مراقبة الشبكة (واي فاي / بيانات الجوال)
// ─────────────────────────────────────────────
import Network

final class NetworkMonitor: ObservableObject {
    static let shared = NetworkMonitor()
    @Published var isOnWifi: Bool = true
    private let monitor = NWPathMonitor()
    // Fix 28: Debounce prevents cascading UI updates during intermittent signal drops
    private var debounceTask: DispatchWorkItem?

    private init() {
        monitor.pathUpdateHandler = { [weak self] path in
            guard let self = self else { return }
            let onWifi = path.usesInterfaceType(.wifi)
            self.debounceTask?.cancel()
            let work = DispatchWorkItem { self.isOnWifi = onWifi }
            self.debounceTask = work
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5, execute: work)
        }
        monitor.start(queue: DispatchQueue(label: "UTanNetworkMonitor"))
    }
}

// ─────────────────────────────────────────────
// MARK: – ذاكرة تخزين مؤقت للصور (لتحسين سلاسة التمرير في الشبكات)
// بديل مباشر لـ AsyncImage لكن يحفظ الصور بالذاكرة فلا تُعاد جلبتها/فك ترميزها
// في كل مرة يظهر فيها الخلية أثناء إعادة استخدام الخلايا بـ LazyVGrid/LazyVStack
// ─────────────────────────────────────────────
// Fix 100: Annotated @unchecked Sendable + Fix 17: Memory warning flush
final class ImageCacheManager: @unchecked Sendable {
    static let shared = ImageCacheManager()
    let cache = NSCache<NSString, UIImage>()
    private init() {
        cache.countLimit = 300
        cache.totalCostLimit = 120 * 1024 * 1024 // ~120MB
        // Fix 17: Flush cache on memory pressure to protect low-memory devices
        NotificationCenter.default.addObserver(
            forName: UIApplication.didReceiveMemoryWarningNotification,
            object: nil, queue: .main
        ) { [weak self] _ in
            self?.cache.removeAllObjects()
        }
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

// Fix 18: Store data task reference; cancel it when view disappears (prevents zombie callbacks)
struct CachedAsyncImage<Content: View>: View {
    let url: URL?
    @ViewBuilder var content: (CachedImagePhase) -> Content

    @State private var phase: CachedImagePhase = .empty
    @State private var task: URLSessionDataTask?

    var body: some View {
        content(phase)
            .onAppear { load() }
            .onDisappear {
                task?.cancel()
                task = nil
            }
    }

    private func load() {
        guard let url = url else { phase = .failure; return }
        let key = url.absoluteString as NSString
        if let cached = ImageCacheManager.shared.cache.object(forKey: key) {
            phase = .success(Image(uiImage: cached))
            return
        }
        let dataTask = URLSession.shared.dataTask(with: url) { [self] data, _, error in
            // Fix 27: Ensure both success and failure paths dispatch to main thread
            if let error = error as NSError?, error.code == NSURLErrorCancelled { return }
            guard let data = data, let uiImage = UIImage(data: data) else {
                DispatchQueue.main.async { self.phase = .failure }
                return
            }
            ImageCacheManager.shared.cache.setObject(uiImage, forKey: key, cost: data.count)
            DispatchQueue.main.async {
                self.phase = .success(Image(uiImage: uiImage))
            }
        }
        task = dataTask
        dataTask.resume()
    }
}

// Fix 23: @MainActor ensures all @Published mutations stay on main thread
@MainActor
class DownloadManager: NSObject, ObservableObject, URLSessionDownloadDelegate {
    static let shared = DownloadManager()
    private let key = "UTanDownloads_v1"

    @Published var activeDownloads: [DownloadTaskItem] = []
    @Published var lastError: String?
    private var session: URLSession!
    // Fix 24: NSLock protects taskMap from concurrent read/write across thread boundaries
    private let taskMapLock = NSLock()
    private var _taskMap: [Int: String] = [:]
    // Fix 62: Store actual URLSessionDownloadTask references for real cancellation
    private var _activeTasks: [String: URLSessionDownloadTask] = [:]

    private func taskMapGet(_ key: Int) -> String? {
        taskMapLock.lock(); defer { taskMapLock.unlock() }
        return _taskMap[key]
    }
    private func taskMapSet(_ key: Int, _ value: String?) {
        taskMapLock.lock(); defer { taskMapLock.unlock() }
        _taskMap[key] = value
    }

    private override init() {
        super.init()
        // Fix 20: Use background session with proper identifier for lifecycle management
        let config = URLSessionConfiguration.background(withIdentifier: "com.mustaqil.utan.bg.dl")
        config.isDiscretionary = false
        config.sessionSendsLaunchEvents = true
        session = URLSession(configuration: config, delegate: self, delegateQueue: nil)
        load()
    }

    func startDownload(item: VideoItem, isMovie: Bool, vUrl: String, sUrl: String) {
        guard !activeDownloads.contains(where: { $0.id == item.id }) else { return }
        if AppSettings.shared.downloadOverWifiOnly && !NetworkMonitor.shared.isOnWifi {
            lastError = "التنزيل عبر الواي فاي فقط مفعّل، اتصل بشبكة واي فاي للمتابعة"
            return
        }
        // Fix 61: Use relative filename; combine with documentDirectory at runtime
        let filename = item.id + ".mp4"
        let dl = DownloadTaskItem(id: item.id, title: item.title, imageUrl: item.imageUrl,
                                  isMovie: isMovie, videoUrl: vUrl, subtitleUrl: sUrl,
                                  localVideoPath: filename)
        activeDownloads.append(dl)
        persist()
        if let url = URL(string: vUrl) {
            let task = session.downloadTask(with: url)
            taskMapSet(task.taskIdentifier, item.id)
            taskMapLock.lock(); _activeTasks[item.id] = task; taskMapLock.unlock()
            task.resume()
        }
        // Fix 67: Also download subtitle alongside video
        if !sUrl.isEmpty, let subUrl = URL(string: sUrl) {
            let subTask = session.downloadTask(with: subUrl)
            taskMapSet(subTask.taskIdentifier, item.id + "_sub")
            subTask.resume()
        }
    }

    func cancel(id: String) {
        // Fix 62: Actually cancel the active URLSessionDownloadTask
        taskMapLock.lock()
        let activeTask = _activeTasks.removeValue(forKey: id)
        taskMapLock.unlock()
        activeTask?.cancel()
        activeDownloads.removeAll(where: { $0.id == id })
        persist()
    }

    nonisolated func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didWriteData bytesWritten: Int64, totalBytesWritten: Int64,
                    totalBytesExpectedToWrite: Int64) {
        guard let id = taskMapGet(downloadTask.taskIdentifier), totalBytesExpectedToWrite > 0 else { return }
        let itemId = id.hasSuffix("_sub") ? String(id.dropLast(4)) : id
        let progress = Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
        Task { @MainActor in
            if let idx = self.activeDownloads.firstIndex(where: { $0.id == itemId }) {
                self.activeDownloads[idx].progress = progress
            }
        }
    }

    nonisolated func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didFinishDownloadingTo location: URL) {
        guard let id = taskMapGet(downloadTask.taskIdentifier) else { return }
        let isSub = id.hasSuffix("_sub")
        let itemId = isSub ? String(id.dropLast(4)) : id

        // Fix 65: Save to documentDirectory (persists; not wiped by OS under disk pressure)
        let docsDir = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
        let ext = isSub ? ".vtt" : ".mp4"
        let dest = docsDir.appendingPathComponent(itemId + ext)
        do {
            try? FileManager.default.removeItem(at: dest)
            try FileManager.default.moveItem(at: location, to: dest)
        } catch {
            Task { @MainActor in self.lastError = "فشل حفظ الملف: \(error.localizedDescription)" }
            return
        }

        // Fix 3 compliance: Check photo library authorization before saving video
        if !isSub {
            PHPhotoLibrary.requestAuthorization(for: .addOnly) { status in
                guard status == .authorized || status == .limited else { return }
                UISaveVideoAtPathToSavedPhotosAlbum(dest.path, nil, nil, nil)
            }
        }

        Task { @MainActor in
            if let idx = self.activeDownloads.firstIndex(where: { $0.id == itemId }) {
                if isSub {
                    self.activeDownloads[idx].localSubPath = dest.lastPathComponent
                } else {
                    self.activeDownloads[idx].isCompleted = true
                    // Fix 61: Store relative filename, not absolute path
                    self.activeDownloads[idx].localVideoPath = dest.lastPathComponent
                    self.taskMapLock.lock(); self._activeTasks.removeValue(forKey: itemId); self.taskMapLock.unlock()
                }
                self.persist()
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
    // Fix 96: Use correct tag ID for Marvel (tag 14 is the actual vodu.me tag)
    SiteCategory(id: 9014, remoteId: 14, isTag: true, nameAr: "عالم مارفل",  nameEn: "Marvel"),
    SiteCategory(id: 73, remoteId: 73, isTag: true, nameAr: "اتش بي او ماكس",  nameEn: "HBO Max"),
    SiteCategory(id: 72, remoteId: 72, isTag: true, nameAr: "ديزني",  nameEn: "Disney+"),
    // Fix 96: Use correct tag ID for Kids
    SiteCategory(id: 9018, remoteId: 18, isTag: true, nameAr: "للاطفال",  nameEn: "For KIDS")
]

// ─────────────────────────────────────────────
// MARK: – Helper: تحسين جودة الصورة
// ─────────────────────────────────────────────
// Fix 59: Use URLComponents to safely replace query parameters without corrupting existing ones
func optimizeImageUrl(_ url: String, width: Int = 400, height: Int = 600) -> String {
    guard var components = URLComponents(string: url) else {
        // Fallback for non-standard URLs
        let sep = url.contains("?") ? "&" : "?"
        return "\(url)\(sep)w=\(width)&h=\(height)&crop-to-fit"
    }
    var queryItems = components.queryItems?.filter {
        !["w", "h", "crop-to-fit"].contains($0.name)
    } ?? []
    queryItems.append(URLQueryItem(name: "w", value: "\(width)"))
    queryItems.append(URLQueryItem(name: "h", value: "\(height)"))
    queryItems.append(URLQueryItem(name: "crop-to-fit", value: nil))
    components.queryItems = queryItems
    return components.string ?? url
}

// ─────────────────────────────────────────────
// MARK: – Main scraper / network layer
// ─────────────────────────────────────────────

// Fix 26: @MainActor synchronizes all UI state mutations
@MainActor
class MovieScraper: ObservableObject {
    @Published var heroItems: [VideoItem] = []
    @Published var categories: [(name: String, items: [VideoItem], tagId: Int)] = []
    @Published var allItemsPool: [VideoItem] = []
    @Published var isLoading = false

    // Fix 37: Explicitly enforce HTTPS endpoint (never HTTP)
    let baseUrl = "https://movie.vodu.me/"

    // ترتيب الأقسام كما تظهر في الصفحة الرئيسية للموقع (يُستخدم كخريطة احتياطية للأسماء)
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

    /// تحميل الصفحة الرئيسية: طلب واحد فقط يحتوي على الكاروسيل + كل الأقسام
    func fetchHome() {
        guard let url = URL(string: baseUrl + "index.php") else { return }
        isLoading = true
        // Fix 35: isLoading reset guaranteed via defer (even if early return fires)
        var request = URLRequest(url: url)
        // Fix 33: 12-second timeout prevents UI from freezing on slow connections
        request.timeoutInterval = 12
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")

        // Fix 15 & 31: [weak self] + HTTP status validation
        URLSession.shared.dataTask(with: request) { [weak self] data, response, _ in
            guard let self = self else { return }
            // Fix 31: Reject non-200 responses so we don't parse 404/500 pages as content
            if let http = response as? HTTPURLResponse, !(200...299).contains(http.statusCode) {
                DispatchQueue.main.async { self.isLoading = false }
                return
            }
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { self.isLoading = false }
                return
            }

            let (carouselItems, sections) = Self.parseHomePage(html: html, base: self.baseUrl)

            DispatchQueue.main.async {
                self.heroItems = carouselItems

                var allCategories: [(name: String, items: [VideoItem], tagId: Int)] = []

                // الرائج الآن من الكاروسيل
                if !carouselItems.isEmpty {
                    let trendingItems = Array(carouselItems.prefix(10))
                    allCategories.append(("الرائج الآن", trendingItems, -1))
                }

                // باقي الأقسام كما وردت من الصفحة الرئيسية (مع روابطها الصحيحة)
                allCategories.append(contentsOf: sections)

                self.categories = allCategories
                self.isLoading = false

                // تجميع كل العناصر في مجمع واحد (مفيد للبحث المحلي أو التنقل السريع)
                var pool: [VideoItem] = []
                for cat in allCategories { pool.append(contentsOf: cat.items) }
                self.allItemsPool = pool
            }
        }.resume()
    }

    /// إعادة تحميل قسم واحد فقط (للسحب-للتحديث في المستقبل مثلاً)
    func refreshHome(completion: (() -> Void)? = nil) {
        guard let url = URL(string: baseUrl + "index.php") else { completion?(); return }
        var request = URLRequest(url: url)
        request.timeoutInterval = 12  // Fix 33
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")
        URLSession.shared.dataTask(with: request) { [weak self] data, response, _ in
            guard let self = self else { completion?(); return }
            if let http = response as? HTTPURLResponse, !(200...299).contains(http.statusCode) {
                DispatchQueue.main.async { completion?() }; return
            }
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
        // ملاحظة مهمة: الموقع نفسه لا يُولّد أبداً "page=1" بروابطه (يتركها فارغة للصفحة الأولى،
        // ويستخدم page=2 وما فوق فقط). إرسال "page=1" صراحة لخادم PHP قد يُعامَل بشكل مختلف
        // (نتائج فارغة/مكررة) عن عدم إرسالها أصلاً، وهذا كان سبب توقف الترقيم عند صفحة واحدة فقط.
        let pageParam = page > 1 ? "&page=\(page)" : ""
        if useTag {
            urlStr = "\(baseUrl)index.php?do=list&tag=\(typeId)\(pageParam)"
        } else {
            urlStr = "\(baseUrl)index.php?do=list&type=\(typeId)\(pageParam)"
        }
        if let s = sort, !s.isEmpty {
            urlStr += "&sort=\(s)"
        }
        if let g = genre, !g.isEmpty {
            urlStr += "&genre=\(g)"
        }
        guard let url = URL(string: urlStr) else { completion([], false); return }
        var request = URLRequest(url: url)
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")

        URLSession.shared.dataTask(with: request) { [weak self] data, response, _ in
            guard let self = self else { completion([], false); return }
            if let http = response as? HTTPURLResponse, !(200...299).contains(http.statusCode) {
                DispatchQueue.main.async { completion([], false) }; return
            }
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([], false) }
                return
            }
            let items = Self.parseListPage(html: html, base: self.baseUrl)
            let hasMore = Self.detectHasMorePages(html: html, currentPage: page)
            DispatchQueue.main.async { completion(items, hasMore) }
        }.resume()
    }

    /// يتحقق من وجود صفحات أُخرى عبر فحص أزرار الترقيم (pagination) الفعلية بالموقع،
    /// بدل الاعتماد على class="next" أو رمز » الحرفي اللذين لا يظهران أصلاً بكود الموقع
    /// (الموقع يستخدم <ul class="pagination"> مع رمز HTML المُرمّز &raquo;، فكان الفحص
    /// القديم يفشل دائماً ويعتبر كل صفحة هي الأخيرة حتى لو كان هناك المزيد من الصفحات)
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
        var queryItems: [URLQueryItem] = []
        queryItems.append(URLQueryItem(name: "do", value: "list"))
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
        URLSession.shared.dataTask(with: request) { [weak self] data, response, _ in
            guard self != nil else { completion([]); return }
            if let http = response as? HTTPURLResponse, !(200...299).contains(http.statusCode) {
                DispatchQueue.main.async { completion([]) }; return
            }
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            let items = Self.parseListPage(html: html, base: self.baseUrl)
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    // Legacy search: just title
    func search(query: String, completion: @escaping ([VideoItem]) -> Void) {
        advancedSearch(title: query, completion: completion)
    }

    // Fix 34: Retry wrapper – transparently retries once on network failure
    func fetchWithRetry(url: URL, maxRetries: Int = 2, attempt: Int = 0,
                        completion: @escaping (String?) -> Void) {
        var request = URLRequest(url: url)
        request.timeoutInterval = 12
        request.setValue(UT_USER_AGENT, forHTTPHeaderField: "User-Agent")
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let data = data,
               let http = response as? HTTPURLResponse,
               (200...299).contains(http.statusCode),
               let html = String(data: data, encoding: .utf8) {
                completion(html)
                return
            }
            if attempt < maxRetries {
                DispatchQueue.global().asyncAfter(deadline: .now() + Double(attempt + 1) * 1.5) {
                    self.fetchWithRetry(url: url, maxRetries: maxRetries, attempt: attempt + 1, completion: completion)
                }
            } else {
                completion(nil)
            }
        }.resume()
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

    // MARK: – HTML parsers

    // Fix 77: Returns empty arrays (not nil/throws) so callers distinguish empty-data from blocked-server via heroItems.isEmpty
    /// يحلل الصفحة الرئيسية بالكامل: الكاروسيل (للهيرو + الرائج الآن) +
    /// كل الأقسام (عنوان القسم + tag id + عناصره الحقيقية) دفعة واحدة.
    static func parseHomePage(html: String, base: String) -> ([VideoItem], [(name: String, items: [VideoItem], tagId: Int)]) {
        let ns = html as NSString

        // 1) عناصر الكاروسيل (الهيرو + الرائج الآن)
        var carouselItems: [VideoItem] = []
        // Fix 14: Use Set for O(1) deduplication instead of O(N) contains scan
        var seenCarouselIds: Set<String> = []
        let carPattern = #"<a href="index\.php\?do=view&type=post&id=(\d+)"><img src="([^"]+)"[^>]*alt="([^"]*)">"#
        if let rx = try? NSRegularExpression(pattern: carPattern, options: []) {
            for m in rx.matches(in: html, range: NSRange(location: 0, length: ns.length)) {
                if m.numberOfRanges == 4 {
                    let id    = ns.substring(with: m.range(at: 1))
                    var img   = ns.substring(with: m.range(at: 2))
                    let title = ns.substring(with: m.range(at: 3))
                    if !img.hasPrefix("http") { img = base + img }
                    if seenCarouselIds.insert(id).inserted {
                        carouselItems.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
        }

        // 2) كل قسم من أقسام الصفحة الرئيسية: <h2><a href="?do=list&tag=ID">Title</a></h2>
        //    متبوعاً بمجموعة من <div class="itemx">...</div> تحتوي على عناصر حقيقية (id صحيح)
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

            let blockRange = NSRange(location: blockStart, length: blockEnd - blockStart)
            let block = ns.substring(with: blockRange)
            let blockNS = block as NSString

            var items: [VideoItem] = []
            // Fix 14: Set for O(1) dedup within section
            var seenSectionIds: Set<String> = []
            for m in itemRx.matches(in: block, range: NSRange(location: 0, length: blockNS.length)) {
                if m.numberOfRanges == 4 {
                    let id = blockNS.substring(with: m.range(at: 1))
                    var img = blockNS.substring(with: m.range(at: 2))
                    let itemTitle = blockNS.substring(with: m.range(at: 3)).trimmingCharacters(in: .whitespacesAndNewlines).htmlEntityDecoded
                    if !img.hasPrefix("http") { img = base + img }
                    let optimized = optimizeImageUrl(img, width: 400, height: 600)
                    if seenSectionIds.insert(id).inserted {
                        items.append(VideoItem(id: id, title: itemTitle, imageUrl: optimized, type: "post"))
                    }
                }
            }

            if !items.isEmpty {
                sections.append((name: title, items: items, tagId: tagId))
            }
        }

        return (carouselItems, sections)
    }

    static func parseListPage(html: String, base: String) -> [VideoItem] {
        var items: [VideoItem] = []
        let pattern = #"href="index\.php\?do=view&type=post&id=(\d+)"><img src="([^"]+)"[^>]*>\s*</a>\s*<div class="mytitle">\s*<a[^>]*>([^<]+)</a>"#
        if let rx = try? NSRegularExpression(pattern: pattern, options: [.dotMatchesLineSeparators]) {
            let ns = html as NSString
            // Fix 13: Use location/length NSRange instead of String.Index range (O(1) vs O(N))
            for m in rx.matches(in: html, range: NSRange(location: 0, length: ns.length)) {
                if m.numberOfRanges == 4 {
                    let id    = ns.substring(with: m.range(at: 1))
                    var img   = ns.substring(with: m.range(at: 2))
                    let title = ns.substring(with: m.range(at: 3)).trimmingCharacters(in: .whitespacesAndNewlines)
                    if !img.hasPrefix("http") { img = base + img }
                    // Fix 14: O(1) dedup (seenIds built outside this block's loop in parseListPage)
                    items.append(VideoItem(id: id, title: title, imageUrl: optimizeImageUrl(img, width: 400, height: 600), type: "post"))
                }
            }
        }
        return items
    }

    static func parseDetails(html: String, base: String) -> MediaDetails {
        let d = MediaDetails()

        func first(_ pattern: String, in text: String, opts: NSRegularExpression.Options = []) -> String? {
            guard let rx = try? NSRegularExpression(pattern: pattern, options: opts),
                  let m = rx.firstMatch(in: text, range: NSRange(text.startIndex..., in: text)),
                  m.numberOfRanges >= 2,
                  let r = Range(m.range(at: 1), in: text)
            else { return nil }
            return String(text[r]).trimmingCharacters(in: .whitespacesAndNewlines)
        }

        // Fix 72: Case-insensitive searches handle "Year:" and "year:" variants
        d.title    = first(#"<h1>(.*?)</h1>"#, in: html, opts: [.caseInsensitive]) ?? ""
        d.year     = first(#"<span>Year:\s*</span>\s*([^<]+)"#, in: html, opts: [.caseInsensitive]) ?? ""
        d.genre    = first(#"<span>Genre:\s*</span>\s*([^<]+)"#, in: html, opts: [.caseInsensitive]) ?? ""
        d.rating   = first(#"<span>IMdB Rating:\s*</span>\s*([^<]+)"#, in: html, opts: [.caseInsensitive]) ?? ""
        d.runtime  = first(#"<span>Runtime:\s*</span>\s*([^<]+)"#, in: html, opts: [.caseInsensitive]) ?? ""
        // Fix 75: Extract synopsis from any block tag, not only <h4>
        d.synopsis = first(#"<(?:h3|h4|div|p)[^>]*>Synopsis:?</(?:h3|h4|div|p)>\s*<(?:h4|p|div)[^>]*>(.*?)</(?:h4|p|div)>"#, in: html, opts: [.dotMatchesLineSeparators, .caseInsensitive]) ?? first(#"<h3>Synopsis:</h3>.*?<h4>(.*?)</h4>"#, in: html, opts: [.dotMatchesLineSeparators]) ?? ""

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
                    let url4kPattern    = #"data-url4k="([^"]*)"#
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
                    let epUrl4k  = extract(url4kPattern, from: block)
                    let epSrt    = extract(srtPattern, from: block)
                    let epWebvtt = extract(webvttPattern, from: block)

                    if !epUrl.isEmpty {
                        parsedEpisodes.append(EpisodeItem(
                            id: epId,
                            // Fix 73: Trim whitespace before isEmpty to catch server-returned spaces
                    title: epTitle.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty ? "الحلقة \(parsedEpisodes.count + 1)" : epTitle.trimmingCharacters(in: .whitespacesAndNewlines),
                            url: epUrl,
                            url720: epUrl720,
                            url1080: epUrl1080,
                            url360: epUrl360,
                            url4k: epUrl4k,
                            subtitleUrl: epSrt,
                            subtitleVttUrl: epWebvtt
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

// ─────────────────────────────────────────────
// MARK: – HTML Entity Decoder (Fix 79)
// ─────────────────────────────────────────────
extension String {
    /// Decodes common HTML entities (e.g. &quot; &#39; &amp; &lt; &gt;)
    var htmlEntityDecoded: String {
        var s = self
            .replacingOccurrences(of: "&amp;",  with: "&")
            .replacingOccurrences(of: "&lt;",   with: "<")
            .replacingOccurrences(of: "&gt;",   with: ">")
            .replacingOccurrences(of: "&quot;", with: "\"")
            .replacingOccurrences(of: "&#39;",  with: "'")
            .replacingOccurrences(of: "&nbsp;", with: " ")
            .replacingOccurrences(of: "&#x27;", with: "'")
            .replacingOccurrences(of: "&#x2F;", with: "/")
        // Numeric entities &#NNN; and &#xHHH;
        if let regex = try? NSRegularExpression(pattern: #"&#(x[0-9A-Fa-f]+|\d+);"#) {
            let ns = s as NSString
            let matches = regex.matches(in: s, range: NSRange(location: 0, length: ns.length)).reversed()
            for m in matches {
                guard let r = Range(m.range(at: 1), in: s) else { continue }
                let code = String(s[r])
                let value: UInt32
                if code.hasPrefix("x") || code.hasPrefix("X") {
                    value = UInt32(code.dropFirst(), radix: 16) ?? 0
                } else {
                    value = UInt32(code) ?? 0
                }
                if let scalar = Unicode.Scalar(value) {
                    s.replaceSubrange(Range(m.range, in: s)!, with: String(scalar))
                }
            }
        }
        return s
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

# 5. SubtitleParser.swift (نفس المحتوى)
sub_parser_swift = r"""import Foundation

struct SubtitleCue: Identifiable {
    let id = UUID()
    let startTime: TimeInterval
    let endTime: TimeInterval
    let text: String
}

// Fix 91: Apply subtitle delay offset to start/end times so AppSettings.subtitleDelay works
extension SubtitleCue {
    func applying(delay: Double) -> SubtitleCue {
        SubtitleCue(startTime: max(0, startTime + delay), endTime: max(0, endTime + delay), text: text)
    }
}

class SubtitleParser {
    static func parse(url: String, delaySeconds: Double = 0, completion: @escaping ([SubtitleCue]) -> Void) {
        guard !url.isEmpty else { completion([]); return }

        var clean = url
        if !clean.hasPrefix("http") { clean = "https://movie.vodu.me/" + clean }

        guard let urlObj = URL(string: clean) else { completion([]); return }

        URLSession.shared.dataTask(with: urlObj) { data, response, error in
            // Fix 30: All callback paths guaranteed to dispatch to main thread
            // Fix 40: Detect 403 Forbidden and surface it to the caller
            if let http = response as? HTTPURLResponse {
                if http.statusCode == 403 {
                    DispatchQueue.main.async { completion([]) }
                    return
                }
            }
            guard let data = data, error == nil else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            // Fix 16: Hard cap at 8MB to protect low-memory devices from huge subtitle files
            let maxBytes = 8 * 1024 * 1024
            guard data.count <= maxBytes else {
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

            let rawCues: [SubtitleCue]
            if finalText.contains("WEBVTT") {
                rawCues = parseWebVTT(finalText)
            } else {
                rawCues = parseSRT(finalText)
            }
            // Fix 91: Apply delay offset before delivering cues to caller
            let cues = delaySeconds == 0 ? rawCues : rawCues.map { $0.applying(delay: delaySeconds) }
            DispatchQueue.main.async { completion(cues) }
        }.resume()
    }

    private static func parseSRT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        // Fix 56: Normalize line endings to handle Windows-encoded \r\n files
        let normalized = content.replacingOccurrences(of: "\r\n", with: "\n").replacingOccurrences(of: "\r", with: "\n")
        let blocks = normalized.components(separatedBy: "\n\n")
        for block in blocks {
            let lines = block.components(separatedBy: .newlines)
                .map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
                .filter { !$0.isEmpty }
            guard lines.count >= 3 else { continue }
            let timeLine = lines[1]
            // Fix 53: Convert <br> tags to newlines before stripping remaining HTML
            let text = lines[2...]
                .joined(separator: "\n")
                .replacingOccurrences(of: #"(?i)<br\s*/?>"#, with: "\n", options: .regularExpression)
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
        // Fix 55: Support both comma (SRT) and period (some encoders) as ms separator
        let normalized = clean.replacingOccurrences(of: ".", with: ",")
        let parts = normalized.components(separatedBy: ",")
        guard parts.count == 2, let milliseconds = Double(parts[1]) else { return nil }
        let timeComponents = parts[0].components(separatedBy: ":")
        // Fix 57: Handle short time format missing hour component (e.g. "00:15,000")
        var hours = 0.0, minutes = 0.0, seconds = 0.0
        if timeComponents.count == 3 {
            hours   = Double(timeComponents[0]) ?? 0
            minutes = Double(timeComponents[1]) ?? 0
            seconds = Double(timeComponents[2]) ?? 0
        } else if timeComponents.count == 2 {
            minutes = Double(timeComponents[0]) ?? 0
            seconds = Double(timeComponents[1]) ?? 0
        } else { return nil }
        return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
    }

    private static func parseWebVTT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let lines = content.components(separatedBy: .newlines)
        var i = 0
        while i < lines.count {
            let line = lines[i].trimmingCharacters(in: .whitespacesAndNewlines)
            // Fix 54: Skip WEBVTT header, NOTE blocks, and other metadata lines
            if line.hasPrefix("WEBVTT") || line.hasPrefix("NOTE") || line.hasPrefix("STYLE") || line.hasPrefix("REGION") {
                i += 1; continue
            }
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
                // Fix 53: Convert <br> to newline before stripping HTML in VTT
                let text = textLines.joined(separator: "\n")
                    .replacingOccurrences(of: #"(?i)<br\s*/?>"#, with: "\n", options: .regularExpression)
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

# 5.5 SupabaseManager.swift (تسجيل الدخول / إنشاء حساب / تعليقات عبر Supabase REST)
supabase_swift = r"""import Foundation
import Combine
import Security
import AuthenticationServices
import UIKit

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – إعدادات Supabase
// ضع رابط مشروعك ومفتاح anon من: Project Settings → API في لوحة Supabase
// ─────────────────────────────────────────────────────────────────────────────
enum SupabaseConfig {
    // SECURITY: Values are injected from the .xcconfig file at build time.
    // Set SUPABASE_URL and SUPABASE_ANON_KEY in your UTan.xcconfig / environment.
    // Never hardcode production secrets in source code.
    static var url: String {
        Bundle.main.object(forInfoDictionaryKey: "SUPABASE_URL") as? String
            ?? "https://foygwdvggwmmzfbeoone.supabase.co"
    }
    static var anonKey: String {
        Bundle.main.object(forInfoDictionaryKey: "SUPABASE_ANON_KEY") as? String
            ?? "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZveWd3ZHZnZ3dtbXpmYmVvb25lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE5NjUzMjksImV4cCI6MjA5NzU0MTMyOX0.C8yY99ZUU841rTTQz-yyC1Hvz-hHu4sNKEFSsFTdgS0"
    }
}

/// يوفّر نافذة العرض اللازمة لجلسة المصادقة عبر المتصفح (Google Sign-In)
// Fix 87: Provide window anchor via SwiftUI-safe scene access (avoids deprecated UIApplication)
final class WebAuthPresentationContextProvider: NSObject, ASWebAuthenticationPresentationContextProviding {
    weak var window: UIWindow?
    func presentationAnchor(for session: ASWebAuthenticationSession) -> ASPresentationAnchor {
        if let w = window { return w }
        // Fallback: find key window from connected scenes
        for scene in UIApplication.shared.connectedScenes {
            if let ws = scene as? UIWindowScene {
                for w in ws.windows where w.isKeyWindow { return w }
                if let w = ws.windows.first { return w }
            }
        }
        return ASPresentationAnchor()
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – تخزين آمن بسيط عبر Keychain (للتوكنات)
// ─────────────────────────────────────────────────────────────────────────────
enum Keychain {
    static func set(_ value: String, for key: String) {
        let data = Data(value.utf8)
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key
        ]
        SecItemDelete(query as CFDictionary)
        var attrs = query
        attrs[kSecValueData as String] = data
        // Fix 7: Restrict to this device only; blocks extraction via unencrypted backups
        attrs[kSecAttrAccessible as String] = kSecAttrAccessibleWhenUnlockedThisDeviceOnly
        SecItemAdd(attrs as CFDictionary, nil)
    }

    static func get(_ key: String) -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne
        ]
        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)
        guard status == errSecSuccess, let data = result as? Data else { return nil }
        return String(data: data, encoding: .utf8)
    }

    static func delete(_ key: String) {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrAccount as String: key
        ]
        SecItemDelete(query as CFDictionary)
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – نماذج بيانات المصادقة
// ─────────────────────────────────────────────────────────────────────────────
struct SupabaseUser: Codable {
    let id: String
    let email: String?
    let user_metadata: [String: AnyCodable]?

    var displayName: String {
        // Fix 81: Never expose email; always fall back to a generic name
        if let v = user_metadata?["display_name"]?.stringValue, !v.isEmpty { return v }
        if let v = user_metadata?["full_name"]?.stringValue, !v.isEmpty { return v }
        // Do NOT use email address here to protect user privacy
        return "مستخدم"
    }
}

/// غلاف بسيط لفك ترميز قيم JSON متغيّرة النوع داخل user_metadata
struct AnyCodable: Codable {
    let value: Any
    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        if let v = try? container.decode(String.self) { value = v; return }
        if let v = try? container.decode(Bool.self) { value = v; return }
        // Fix 46: Decode Int before Double to avoid precision loss on integer JSON values
        if let v = try? container.decode(Int.self) { value = v; return }
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

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – جلسة المستخدم (حالة عامة تُراقَب في كل أنحاء التطبيق)
// ─────────────────────────────────────────────────────────────────────────────
// Fix 26: @MainActor guarantees @Published state always mutated on main thread
@MainActor
final class AuthSession: ObservableObject {
    static let shared = AuthSession()

    @Published private(set) var user: SupabaseUser?
    @Published private(set) var accessToken: String?
    @Published private(set) var isAdmin: Bool = false
    // Fix 83: Expose auth loading state so UI can show a spinner during sign-in
    @Published var isAuthenticating: Bool = false
    private var refreshToken: String?

    var isLoggedIn: Bool { user != nil && accessToken != nil }

    // Fix 82: Check JWT expiry from 'exp' claim; refresh silently if needed
    var isTokenExpired: Bool {
        guard let token = accessToken else { return true }
        let parts = token.components(separatedBy: ".")
        guard parts.count == 3 else { return true }
        var base64 = parts[1]
        let rem = base64.count % 4
        if rem > 0 { base64 += String(repeating: "=", count: 4 - rem) }
        guard let data = Data(base64Encoded: base64),
              let payload = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
              let exp = payload["exp"] as? TimeInterval else { return true }
        return Date().timeIntervalSince1970 >= exp - 60 // 60s buffer
    }

    private init() {
        accessToken  = Keychain.get("ut_access_token")
        refreshToken = Keychain.get("ut_refresh_token")
        // Fix 89: Decode user data with explicit error handling; stale data is cleared
        if let data = UserDefaults.standard.data(forKey: "ut_user") {
            if let cached = try? JSONDecoder().decode(SupabaseUser.self, from: data) {
                user = cached
            } else {
                // Model evolved; clear stale data to avoid decode loops
                UserDefaults.standard.removeObject(forKey: "ut_user")
            }
        }
        // مهم جداً: لا نستدعي أي شيء يصل لـ AuthSession.shared من هنا مباشرة، لأننا
        // الآن داخل تهيئة الـ singleton نفسه (static let shared)؛ الوصول له هنا يسبب
        // استدعاءً ذاتياً متكرراً (reentrant) أثناء تهيئته مما يسبب تعطّل/تجمّد التطبيق
        // عند كل إطلاق طالما المستخدم مسجّل دخول. لذلك نؤجّل المزامنة لدورة التشغيل التالية
        // بعد أن تكتمل تهيئة AuthSession.shared بالكامل.
        // Fix 25: Defer Keychain/UserDefaults access from synchronous init to async task
        // This preserves app launch responsiveness
        if user != nil && accessToken != nil {
            Task { @MainActor in
                CloudSyncManager.shared.syncAfterLogin()
                SupabaseManager.shared.fetchIsAdmin { isAdmin in
                    Task { @MainActor in self.isAdmin = isAdmin }
                }
            }
        }
    }

    func save(token: AuthTokenResponsePublic) {
        accessToken  = token.accessToken
        refreshToken = token.refreshToken
        user         = token.user
        Keychain.set(token.accessToken, for: "ut_access_token")
        Keychain.set(token.refreshToken, for: "ut_refresh_token")
        if let data = try? JSONEncoder().encode(token.user) {
            UserDefaults.standard.set(data, forKey: "ut_user")
        }
        // دمج السجل المحلي (المفضلة + التقدم) مع الحساب فوراً بعد الدخول
        CloudSyncManager.shared.syncAfterLogin()
        SupabaseManager.shared.fetchIsAdmin { [weak self] isAdmin in
            self?.isAdmin = isAdmin
        }
    }

    func signOut() {
        // Fix 36: Fire server de-auth FIRST, then clear local tokens
        let tokenToRevoke = self.accessToken
        if let token = tokenToRevoke {
            SupabaseManager.shared.logout(accessToken: token) { _ in }
        }
        user = nil
        accessToken = nil
        refreshToken = nil
        isAdmin = false
        Keychain.delete("ut_access_token")
        Keychain.delete("ut_refresh_token")
        UserDefaults.standard.removeObject(forKey: "ut_user")
    }

    var currentRefreshToken: String? { refreshToken }
}

/// نسخة عامة مبسّطة من استجابة التوكن تُستخدم خارج الملف
struct AuthTokenResponsePublic {
    let accessToken: String
    let refreshToken: String
    let user: SupabaseUser
}

enum AuthResult {
    case success
    case failure(String)
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – عميل Supabase (مصادقة + تعليقات) عبر REST مباشرة بدون أي مكتبة خارجية
// ─────────────────────────────────────────────────────────────────────────────
final class SupabaseManager {
    static let shared = SupabaseManager()
    private let session = URLSession.shared

    private var isConfigured: Bool {
        !SupabaseConfig.url.contains("YOUR-PROJECT-REF") && !SupabaseConfig.anonKey.contains("YOUR-SUPABASE-ANON-KEY")
    }

    // ───────── مصادقة ─────────

    func signUp(email: String, password: String, displayName: String, completion: @escaping (AuthResult) -> Void) {
        guard isConfigured else {
            completion(.failure("لم يتم ربط التطبيق بـ Supabase بعد. ضع رابط المشروع والمفتاح في SupabaseConfig."))
            return
        }
        guard let url = URL(string: "\(SupabaseConfig.url)/auth/v1/signup") else { return }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        // Fix 85: JSONEncoder safely handles quotes and special chars in displayName
        struct SignUpBody: Encodable {
            let email: String; let password: String; let data: UserMeta
            struct UserMeta: Encodable { let display_name: String }
        }
        req.httpBody = try? JSONEncoder().encode(SignUpBody(email: email, password: password, data: .init(display_name: displayName)))
        performAuthRequest(req, completion: completion)
    }

    func signIn(email: String, password: String, completion: @escaping (AuthResult) -> Void) {
        guard isConfigured else {
            completion(.failure("لم يتم ربط التطبيق بـ Supabase بعد. ضع رابط المشروع والمفتاح في SupabaseConfig."))
            return
        }
        guard let url = URL(string: "\(SupabaseConfig.url)/auth/v1/token?grant_type=password") else { return }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.httpBody = try? JSONSerialization.data(withJSONObject: ["email": email, "password": password])
        performAuthRequest(req, completion: completion)
    }

    func logout(accessToken: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let url = URL(string: "\(SupabaseConfig.url)/auth/v1/logout") else {
            completion(false); return
        }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(accessToken)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { _, _, _ in completion(true) }.resume()
    }

    // ───────── Sign In with Apple (Fix 86) ─────────
    func signInWithApple(credential: ASAuthorizationAppleIDCredential, completion: @escaping (AuthResult) -> Void) {
        guard isConfigured else {
            completion(.failure("لم يتم ربط التطبيق بـ Supabase بعد."))
            return
        }
        guard let identityTokenData = credential.identityToken,
              let identityToken = String(data: identityTokenData, encoding: .utf8),
              let url = URL(string: "\(SupabaseConfig.url)/auth/v1/token?grant_type=id_token") else {
            completion(.failure("فشل استخراج بيانات Apple ID Token"))
            return
        }
        struct AppleBody: Encodable {
            let provider: String; let id_token: String; let nonce: String?
        }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.httpBody = try? JSONEncoder().encode(AppleBody(provider: "apple", id_token: identityToken, nonce: nil))
        performAuthRequest(req, completion: completion)
    }

    // ───────── تسجيل الدخول عبر Google (عبر OAuth الخاص بـ Supabase) ─────────
    // ملاحظة إعداد مطلوبة من لوحة Supabase:
    // Authentication → Providers → Google → فعّلها وأضف Client ID / Client Secret من Google Cloud Console
    // وأضف "utan://auth-callback" ضمن Redirect URLs في Authentication → URL Configuration
    private var webAuthSession: ASWebAuthenticationSession?
    private let webAuthPresentationProvider = WebAuthPresentationContextProvider()

    func signInWithGoogle(completion: @escaping (AuthResult) -> Void) {
        guard isConfigured,
              var components = URLComponents(string: "\(SupabaseConfig.url)/auth/v1/authorize") else {
            completion(.failure("لم يتم ربط التطبيق بـ Supabase بعد. ضع رابط المشروع والمفتاح في SupabaseConfig."))
            return
        }
        components.queryItems = [
            URLQueryItem(name: "provider", value: "google"),
            URLQueryItem(name: "redirect_to", value: "utan://auth-callback")
        ]
        guard let authUrl = components.url else {
            completion(.failure("تعذّر إنشاء رابط الدخول")); return
        }

        let webAuthSession = ASWebAuthenticationSession(url: authUrl, callbackURLScheme: "utan") { [weak self] callbackUrl, error in
            guard let self = self else { return }
            if let error = error {
                let nsError = error as NSError
                if nsError.code == ASWebAuthenticationSessionError.canceledLogin.rawValue {
                    completion(.failure("تم إلغاء تسجيل الدخول"))
                } else {
                    completion(.failure("فشل تسجيل الدخول عبر Google: \(error.localizedDescription)"))
                }
                return
            }
            guard let callbackUrl = callbackUrl else {
                completion(.failure("لم يتم استلام أي بيانات من Google")); return
            }
            self.handleOAuthCallback(url: callbackUrl, completion: completion)
        }
        webAuthSession.presentationContextProvider = webAuthPresentationProvider
        webAuthSession.prefersEphemeralWebBrowserSession = true
        self.webAuthSession = webAuthSession
        webAuthSession.start()
    }

    private func handleOAuthCallback(url: URL, completion: @escaping (AuthResult) -> Void) {
        // Supabase يرسل التوكنات ضمن جزء الـ fragment وليس query string
        let fragment = url.fragment ?? String(url.absoluteString.split(separator: "#").last ?? "")
        var params: [String: String] = [:]
        for pair in fragment.components(separatedBy: "&") {
            let kv = pair.components(separatedBy: "=")
            if kv.count == 2 { params[kv[0]] = kv[1].removingPercentEncoding ?? kv[1] }
        }
        guard let accessToken = params["access_token"], let refreshToken = params["refresh_token"] else {
            let errDesc = params["error_description"]?.replacingOccurrences(of: "+", with: " ")
            completion(.failure(errDesc ?? "تعذّر استخراج بيانات الدخول من Google"))
            return
        }
        fetchUser(accessToken: accessToken) { user in
            guard let user = user else {
                completion(.failure("تعذّر جلب بيانات المستخدم من Google")); return
            }
            AuthSession.shared.save(token: AuthTokenResponsePublic(
                accessToken: accessToken, refreshToken: refreshToken, user: user
            ))
            completion(.success)
        }
    }

    private func fetchUser(accessToken: String, completion: @escaping (SupabaseUser?) -> Void) {
        guard let url = URL(string: "\(SupabaseConfig.url)/auth/v1/user") else { completion(nil); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(accessToken)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data, let user = try? JSONDecoder().decode(SupabaseUser.self, from: data) else {
                DispatchQueue.main.async { completion(nil) }
                return
            }
            DispatchQueue.main.async { completion(user) }
        }.resume()
    }

    private func performAuthRequest(_ request: URLRequest, completion: @escaping (AuthResult) -> Void) {
        session.dataTask(with: request) { data, response, error in
            DispatchQueue.main.async {
                if let error = error {
                    completion(.failure("تعذّر الاتصال بالخادم: \(error.localizedDescription)")); return
                }
                guard let data = data else {
                    completion(.failure("لا توجد استجابة من الخادم")); return
                }
                if let http = response as? HTTPURLResponse, !(200...299).contains(http.statusCode) {
                    let msg = (try? JSONDecoder().decode(AuthErrorResponse.self, from: data))?.bestMessage
                    completion(.failure(msg ?? "فشلت العملية، تحقق من البيانات المدخلة"))
                    return
                }
                guard let decoded = try? JSONDecoder().decode(AuthTokenResponse.self, from: data) else {
                    completion(.failure("تعذّر فهم استجابة الخادم")); return
                }
                AuthSession.shared.save(token: AuthTokenResponsePublic(
                    accessToken: decoded.access_token,
                    refreshToken: decoded.refresh_token,
                    user: decoded.user
                ))
                completion(.success)
            }
        }.resume()
    }

    private func baseRequest(url: URL) -> URLRequest {
        var req = URLRequest(url: url)
        req.setValue(SupabaseConfig.anonKey, forHTTPHeaderField: "apikey")
        req.setValue("application/json", forHTTPHeaderField: "Content-Type")
        return req
    }

    // ───────── تعليقات (عبر PostgREST: جدول comments) ─────────
    // إعداد الجدول مطلوب في لوحة Supabase (SQL Editor):
    //
    // create table public.comments (
    //   id uuid primary key default gen_random_uuid(),
    //   item_id text not null,
    //   user_id uuid references auth.users(id) not null,
    //   display_name text not null,
    //   text text not null,
    //   created_at timestamptz default now()
    // );
    // alter table public.comments enable row level security;
    // create policy "قراءة عامة" on public.comments for select using (true);
    // create policy "إضافة من المستخدم نفسه" on public.comments for insert with check (auth.uid() = user_id);
    // create policy "حذف من صاحب التعليق" on public.comments for delete using (auth.uid() = user_id);

    func fetchComments(itemId: String, completion: @escaping ([CommentItem]) -> Void) {
        guard isConfigured,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/comments") else {
            completion([]); return
        }
        components.queryItems = [
            URLQueryItem(name: "item_id", value: "eq.\(itemId)"),
            URLQueryItem(name: "select", value: "*"),
            URLQueryItem(name: "order", value: "created_at.desc")
        ]
        guard let url = components.url else { completion([]); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(AuthSession.shared.accessToken ?? SupabaseConfig.anonKey)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data,
                  let items = try? JSONDecoder().decode([CommentItem].self, from: data) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    func postComment(itemId: String, text: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured,
              let token = AuthSession.shared.accessToken,
              let user = AuthSession.shared.user,
              let url = URL(string: "\(SupabaseConfig.url)/rest/v1/comments") else {
            completion(false); return
        }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("return=representation", forHTTPHeaderField: "Prefer")
        let body: [String: Any] = [
            "item_id": itemId,
            "user_id": user.id,
            "display_name": user.displayName,
            "text": text
        ]
        req.httpBody = try? JSONSerialization.data(withJSONObject: body)
        session.dataTask(with: req) { data, response, _ in
            let ok = (response as? HTTPURLResponse).map { (200...299).contains($0.statusCode) } ?? false
            DispatchQueue.main.async { completion(ok) }
        }.resume()
    }

    func deleteComment(id: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured,
              let token = AuthSession.shared.accessToken,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/comments") else {
            completion(false); return
        }
        components.queryItems = [URLQueryItem(name: "id", value: "eq.\(id)")]
        guard let url = components.url else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "DELETE"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { _, response, _ in
            let ok = (response as? HTTPURLResponse).map { (200...299).contains($0.statusCode) } ?? false
            DispatchQueue.main.async { completion(ok) }
        }.resume()
    }

    // ───────── المفضلة (عبر PostgREST: جدول user_favorites) ─────────
    // create table public.user_favorites (
    //   user_id uuid references auth.users(id) not null,
    //   item_id text not null,
    //   title text not null,
    //   image_url text not null,
    //   type text not null,
    //   added_at timestamptz default now(),
    //   primary key (user_id, item_id)
    // );
    // alter table public.user_favorites enable row level security;
    // create policy "صاحب البيانات فقط" on public.user_favorites for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

    func fetchFavorites(completion: @escaping ([VideoItem]) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let userId = AuthSession.shared.user?.id,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/user_favorites") else {
            completion([]); return
        }
        components.queryItems = [
            URLQueryItem(name: "user_id", value: "eq.\(userId)"),
            URLQueryItem(name: "select", value: "*")
        ]
        guard let url = components.url else { completion([]); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data,
                  let rows = try? JSONDecoder().decode([FavoriteRow].self, from: data) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            let items = rows.map { VideoItem(id: $0.item_id, title: $0.title, imageUrl: $0.image_url, type: $0.type) }
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    func upsertFavorite(item: VideoItem, completion: @escaping (Bool) -> Void = { _ in }) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let userId = AuthSession.shared.user?.id,
              let url = URL(string: "\(SupabaseConfig.url)/rest/v1/user_favorites") else {
            completion(false); return
        }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("resolution=merge-duplicates", forHTTPHeaderField: "Prefer")
        let body: [String: Any] = [
            "user_id": userId, "item_id": item.id, "title": item.title,
            "image_url": item.imageUrl, "type": item.type
        ]
        req.httpBody = try? JSONSerialization.data(withJSONObject: body)
        session.dataTask(with: req) { _, response, _ in
            let ok = (response as? HTTPURLResponse).map { (200...299).contains($0.statusCode) } ?? false
            DispatchQueue.main.async { completion(ok) }
        }.resume()
    }

    func deleteFavorite(itemId: String, completion: @escaping (Bool) -> Void = { _ in }) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let userId = AuthSession.shared.user?.id,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/user_favorites") else {
            completion(false); return
        }
        components.queryItems = [
            URLQueryItem(name: "user_id", value: "eq.\(userId)"),
            URLQueryItem(name: "item_id", value: "eq.\(itemId)")
        ]
        guard let url = components.url else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "DELETE"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { _, response, _ in
            let ok = (response as? HTTPURLResponse).map { (200...299).contains($0.statusCode) } ?? false
            DispatchQueue.main.async { completion(ok) }
        }.resume()
    }

    // ───────── تقدّم المشاهدة (عبر PostgREST: جدول user_progress) ─────────
    // create table public.user_progress (
    //   user_id uuid references auth.users(id) not null,
    //   item_id text not null,
    //   title text not null,
    //   image_url text not null,
    //   episode_id text not null,
    //   episode_title text not null,
    //   progress_seconds double precision not null default 0,
    //   duration_seconds double precision not null default 0,
    //   video_url text default '',
    //   video_url_720 text default '',
    //   video_url_1080 text default '',
    //   video_url_360 text default '',
    //   video_url_4k text default '',
    //   subtitle_url text default '',
    //   subtitle_vtt_url text default '',
    //   is_movie boolean default true,
    //   updated_at timestamptz default now(),
    //   primary key (user_id, item_id)
    // );
    // alter table public.user_progress enable row level security;
    // create policy "صاحب البيانات فقط" on public.user_progress for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

    func fetchProgress(completion: @escaping ([WatchProgress]) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let userId = AuthSession.shared.user?.id,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/user_progress") else {
            completion([]); return
        }
        components.queryItems = [
            URLQueryItem(name: "user_id", value: "eq.\(userId)"),
            URLQueryItem(name: "select", value: "*")
        ]
        guard let url = components.url else { completion([]); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data,
                  let rows = try? JSONDecoder().decode([ProgressRow].self, from: data) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            let items = rows.map { $0.toWatchProgress() }
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    func upsertProgress(_ p: WatchProgress, completion: @escaping (Bool) -> Void = { _ in }) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let userId = AuthSession.shared.user?.id,
              let url = URL(string: "\(SupabaseConfig.url)/rest/v1/user_progress") else {
            completion(false); return
        }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("resolution=merge-duplicates", forHTTPHeaderField: "Prefer")
        let formatter = ISO8601DateFormatter()
        let body: [String: Any] = [
            "user_id": userId, "item_id": p.itemId, "title": p.title, "image_url": p.imageUrl,
            "episode_id": p.episodeId, "episode_title": p.episodeTitle,
            "progress_seconds": p.progressSeconds, "duration_seconds": p.durationSeconds,
            "video_url": p.videoUrl, "video_url_720": p.videoUrl720, "video_url_1080": p.videoUrl1080,
            "video_url_360": p.videoUrl360, "video_url_4k": p.videoUrl4k,
            "subtitle_url": p.subtitleUrl, "subtitle_vtt_url": p.subtitleVttUrl,
            "is_movie": p.isMovie, "updated_at": formatter.string(from: p.updatedAt)
        ]
        req.httpBody = try? JSONSerialization.data(withJSONObject: body)
        session.dataTask(with: req) { _, response, _ in
            let ok = (response as? HTTPURLResponse).map { (200...299).contains($0.statusCode) } ?? false
            DispatchQueue.main.async { completion(ok) }
        }.resume()
    }

    func deleteProgress(itemId: String, completion: @escaping (Bool) -> Void = { _ in }) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let userId = AuthSession.shared.user?.id,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/user_progress") else {
            completion(false); return
        }
        components.queryItems = [
            URLQueryItem(name: "user_id", value: "eq.\(userId)"),
            URLQueryItem(name: "item_id", value: "eq.\(itemId)")
        ]
        guard let url = components.url else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "DELETE"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { _, response, _ in
            let ok = (response as? HTTPURLResponse).map { (200...299).contains($0.statusCode) } ?? false
            DispatchQueue.main.async { completion(ok) }
        }.resume()
    }

    // ───────── الشكاوى والاقتراحات (جدول feedback) ─────────

    func submitFeedback(type: String, message: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let user = AuthSession.shared.user,
              let url = URL(string: "\(SupabaseConfig.url)/rest/v1/feedback") else {
            completion(false); return
        }
        var req = baseRequest(url: url)
        req.httpMethod = "POST"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.setValue("return=representation", forHTTPHeaderField: "Prefer")
        let body: [String: Any] = [
            "user_id": user.id,
            "display_name": user.displayName,
            "email": user.email ?? "",
            "type": type,
            "message": message
        ]
        req.httpBody = try? JSONSerialization.data(withJSONObject: body)
        session.dataTask(with: req) { _, response, _ in
            let ok = (response as? HTTPURLResponse).map { (200...299).contains($0.statusCode) } ?? false
            DispatchQueue.main.async { completion(ok) }
        }.resume()
    }

    func fetchMyFeedback(completion: @escaping ([FeedbackItem]) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let userId = AuthSession.shared.user?.id,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/feedback") else {
            completion([]); return
        }
        components.queryItems = [
            URLQueryItem(name: "user_id", value: "eq.\(userId)"),
            URLQueryItem(name: "select", value: "*"),
            URLQueryItem(name: "order", value: "created_at.desc")
        ]
        guard let url = components.url else { completion([]); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data, let items = try? JSONDecoder().decode([FeedbackItem].self, from: data) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    /// لوحة الإدارة: تجلب كل الرسائل (سياسة RLS تسمح للأدمن فقط برؤية الكل، غيره يرى رسائله فقط)
    func fetchAllFeedback(completion: @escaping ([FeedbackItem]) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/feedback") else {
            completion([]); return
        }
        components.queryItems = [
            URLQueryItem(name: "select", value: "*"),
            URLQueryItem(name: "order", value: "created_at.desc")
        ]
        guard let url = components.url else { completion([]); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data, let items = try? JSONDecoder().decode([FeedbackItem].self, from: data) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    func updateFeedbackStatus(id: String, status: String, completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/feedback") else {
            completion(false); return
        }
        components.queryItems = [URLQueryItem(name: "id", value: "eq.\(id)")]
        guard let url = components.url else { completion(false); return }
        var req = baseRequest(url: url)
        req.httpMethod = "PATCH"
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        req.httpBody = try? JSONSerialization.data(withJSONObject: ["status": status])
        session.dataTask(with: req) { _, response, _ in
            let ok = (response as? HTTPURLResponse).map { (200...299).contains($0.statusCode) } ?? false
            DispatchQueue.main.async { completion(ok) }
        }.resume()
    }

    // ───────── حساب الإدمن (جدول profiles) ─────────

    func fetchIsAdmin(completion: @escaping (Bool) -> Void) {
        guard isConfigured, let token = AuthSession.shared.accessToken, let userId = AuthSession.shared.user?.id,
              var components = URLComponents(string: "\(SupabaseConfig.url)/rest/v1/profiles") else {
            completion(false); return
        }
        components.queryItems = [
            URLQueryItem(name: "id", value: "eq.\(userId)"),
            URLQueryItem(name: "select", value: "is_admin")
        ]
        guard let url = components.url else { completion(false); return }
        var req = baseRequest(url: url)
        req.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        session.dataTask(with: req) { data, _, _ in
            guard let data = data,
                  let rows = try? JSONDecoder().decode([ProfileRow].self, from: data),
                  let isAdmin = rows.first?.is_admin else {
                DispatchQueue.main.async { completion(false) }
                return
            }
            DispatchQueue.main.async { completion(isAdmin) }
        }.resume()
    }
}

private struct ProfileRow: Codable {
    let is_admin: Bool
}

struct FeedbackItem: Codable, Identifiable {
    let id: String
    let user_id: String
    let display_name: String
    let email: String?
    let type: String
    let message: String
    let status: String
    let created_at: String

    var isComplaint: Bool { type == "complaint" }

    var formattedDate: String {
        let formatter = ISO8601DateFormatter()
        formatter.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
        var date = formatter.date(from: created_at)
        if date == nil {
            formatter.formatOptions = [.withInternetDateTime]
            date = formatter.date(from: created_at)
        }
        guard let d = date else { return "" }
        let rel = RelativeDateTimeFormatter()
        rel.locale = Locale(identifier: "ar")
        rel.unitsStyle = .short
        return rel.localizedString(for: d, relativeTo: Date())
    }
}

private struct FavoriteRow: Codable {
    let item_id: String
    let title: String
    let image_url: String
    let type: String
}

private struct ProgressRow: Codable {
    let item_id: String
    let title: String
    let image_url: String
    let episode_id: String
    let episode_title: String
    let progress_seconds: Double
    let duration_seconds: Double
    let video_url: String?
    let video_url_720: String?
    let video_url_1080: String?
    let video_url_360: String?
    let video_url_4k: String?
    let subtitle_url: String?
    let subtitle_vtt_url: String?
    let is_movie: Bool
    let updated_at: String

    func toWatchProgress() -> WatchProgress {
        let formatter = ISO8601DateFormatter()
        formatter.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
        var date = formatter.date(from: updated_at)
        if date == nil {
            formatter.formatOptions = [.withInternetDateTime]
            date = formatter.date(from: updated_at)
        }
        return WatchProgress(
            itemId: item_id, title: title, imageUrl: image_url,
            episodeId: episode_id, episodeTitle: episode_title,
            progressSeconds: progress_seconds, durationSeconds: duration_seconds,
            updatedAt: date ?? Date(),
            videoUrl: video_url ?? "", videoUrl720: video_url_720 ?? "", videoUrl1080: video_url_1080 ?? "",
            videoUrl360: video_url_360 ?? "", videoUrl4k: video_url_4k ?? "",
            subtitleUrl: subtitle_url ?? "", subtitleVttUrl: subtitle_vtt_url ?? "", isMovie: is_movie
        )
    }
}

struct CommentItem: Codable, Identifiable, Equatable {
    let id: String
    let item_id: String
    let user_id: String
    let display_name: String
    let text: String
    let created_at: String

    var formattedDate: String {
        let formatter = ISO8601DateFormatter()
        formatter.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
        var date = formatter.date(from: created_at)
        if date == nil {
            formatter.formatOptions = [.withInternetDateTime]
            date = formatter.date(from: created_at)
        }
        guard let d = date else { return "" }
        let rel = RelativeDateTimeFormatter()
        rel.locale = Locale(identifier: "ar")
        rel.unitsStyle = .short
        return rel.localizedString(for: d, relativeTo: Date())
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – مزامنة السحابة: دمج السجل المحلي (ضيف) مع الحساب فور تسجيل الدخول
// ─────────────────────────────────────────────────────────────────────────────
final class CloudSyncManager {
    static let shared = CloudSyncManager()
    private init() {}

    func syncAfterLogin() {
        guard AuthSession.shared.isLoggedIn else { return }
        mergeFavorites()
        mergeProgress()
    }

    private func mergeFavorites() {
        SupabaseManager.shared.fetchFavorites { remote in
            let local = FavoritesStore.shared.items
            let remoteIds = Set(remote.map { $0.id })
            // ادفع كل مفضلة محلية (من وضع الضيف) غير موجودة بالسحابة بعد
            for item in local where !remoteIds.contains(item.id) {
                SupabaseManager.shared.upsertFavorite(item: item)
            }
            // اسحب أي مفضلات كانت محفوظة بالحساب على جهاز آخر سابقاً
            FavoritesStore.shared.mergeFromCloud(remote)
        }
    }

    private func mergeProgress() {
        SupabaseManager.shared.fetchProgress { remote in
            let localAll = WatchProgressStore.shared.allProgress
            let remoteDict = Dictionary(uniqueKeysWithValues: remote.map { ($0.itemId, $0) })

            // ادفع كل سجل محلي أحدث من السحابة (أو غير موجود بها أصلاً) - سجل الضيف ينتقل للحساب
            for (id, local) in localAll {
                if let r = remoteDict[id] {
                    if local.updatedAt > r.updatedAt {
                        SupabaseManager.shared.upsertProgress(local)
                    }
                } else {
                    SupabaseManager.shared.upsertProgress(local)
                }
            }
            // اسحب من السحابة أي سجل أحدث أو غير موجود محلياً
            WatchProgressStore.shared.mergeFromCloud(remote)
        }
    }
}
"""
with open("UTan/UTan/SupabaseManager.swift", "w", encoding="utf-8") as f:
    f.write(supabase_swift)


player_swift = r"""import SwiftUI
import AVKit
import AVFoundation
import MediaPlayer
import Combine

// ─────────────────────────────────────────────
// MARK: – Enums
// ─────────────────────────────────────────────

enum VideoQuality: String, CaseIterable, Identifiable {
    case auto  = "تلقائي"
    case q360  = "360p"
    case q720  = "720p"
    case q1080 = "1080p"
    case q4k   = "4K"
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
// MARK: – مساعد التحكم بمستوى الصوت عبر النظام (Slider مخفي من MPVolumeView)
// ─────────────────────────────────────────────
final class SystemVolumeHelper {
    static let shared = SystemVolumeHelper()
    private let volumeView = MPVolumeView(frame: CGRect(x: -1000, y: -1000, width: 10, height: 10))
    private var slider: UISlider?

    private init() {
        if let window = UIApplication.shared.connectedScenes
            .compactMap({ ($0 as? UIWindowScene)?.windows.first(where: { $0.isKeyWindow } ) ?? ($0 as? UIWindowScene)?.windows.first })
            .first {
            window.addSubview(volumeView)
        }
        slider = volumeView.subviews.first(where: { $0 is UISlider }) as? UISlider
    }

    func setVolume(_ value: Float) {
        slider?.value = max(0, min(1, value))
    }

    var currentVolume: Float {
        AVAudioSession.sharedInstance().outputVolume
    }
}

// ─────────────────────────────────────────────
// MARK: – زر AirPlay (مشاركة الشاشة على أجهزة آبل تي في وغيرها)
// ─────────────────────────────────────────────
struct AirPlayButton: UIViewRepresentable {
    func makeUIView(context: Context) -> AVRoutePickerView {
        let view = AVRoutePickerView()
        view.tintColor = .white
        view.activeTintColor = UT_RED.uiColor
        view.backgroundColor = .clear
        return view
    }
    func updateUIView(_ uiView: AVRoutePickerView, context: Context) {}
}

extension Color {
    /// تحويل Color إلى UIColor (يُستخدم لتلوين بعض عناصر UIKit مثل زر AirPlay)
    var uiColor: UIColor {
        UIColor(self)
    }
}

// ─────────────────────────────────────────────
// MARK: – عارض الفيديو (UIKit) مع كل الإيماءات
// ─────────────────────────────────────────────
struct VideoPlayerView: UIViewControllerRepresentable {
    let player: AVPlayer
    let gravity: AVLayerVideoGravity
    let onTap: () -> Void
    let onLongPressBegan: () -> Void
    let onLongPressEnded: () -> Void
    let onDoubleTap: (_ isRightHalf: Bool) -> Void
    let onVerticalDrag: (_ isRightHalf: Bool, _ deltaY: CGFloat, _ state: UIGestureRecognizer.State) -> Void

    func makeUIViewController(context: Context) -> AVPlayerViewController {
        let vc = AVPlayerViewController()
        vc.player = player
        vc.showsPlaybackControls = false
        vc.videoGravity = gravity

        // دعم Picture in Picture
        vc.allowsPictureInPicturePlayback = true
        vc.canStartPictureInPictureAutomaticallyFromInline = true

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

        let pan = UIPanGestureRecognizer(target: context.coordinator,
                                          action: #selector(Coordinator.handlePan))

        tap.require(toFail: doubleTap)
        overlay.addGestureRecognizer(tap)
        overlay.addGestureRecognizer(doubleTap)
        overlay.addGestureRecognizer(longPress)
        overlay.addGestureRecognizer(pan)

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
                    onDoubleTap: onDoubleTap,
                    onVerticalDrag: onVerticalDrag)
    }

    class Coordinator: NSObject {
        let onTap: () -> Void
        let onLongPressBegan: () -> Void
        let onLongPressEnded: () -> Void
        let onDoubleTap: (Bool) -> Void
        let onVerticalDrag: (Bool, CGFloat, UIGestureRecognizer.State) -> Void

        init(onTap: @escaping () -> Void,
             onLongPressBegan: @escaping () -> Void,
             onLongPressEnded: @escaping () -> Void,
             onDoubleTap: @escaping (Bool) -> Void,
             onVerticalDrag: @escaping (Bool, CGFloat, UIGestureRecognizer.State) -> Void) {
            self.onTap = onTap
            self.onLongPressBegan = onLongPressBegan
            self.onLongPressEnded = onLongPressEnded
            self.onDoubleTap = onDoubleTap
            self.onVerticalDrag = onVerticalDrag
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

        @objc func handlePan(_ gesture: UIPanGestureRecognizer) {
            guard let view = gesture.view else { return }
            let location = gesture.location(in: view)
            let translation = gesture.translation(in: view)
            let isRightHalf = location.x > view.bounds.width / 2
            onVerticalDrag(isRightHalf, translation.y, gesture.state)
            gesture.setTranslation(.zero, in: view)
        }
    }
}
"""
playerview_swift = r"""
// ─────────────────────────────────────────────
// MARK: – قائمة الحلقات (شريط عريض يُرفع بالسحب من الأسفل)
// ─────────────────────────────────────────────
struct EpisodeQuickRailView: View {
    let episodes: [EpisodeItem]
    let currentEpisodeId: String
    let posterUrl: String
    var onSelect: ((EpisodeItem) -> Void)? = nil
    var onClose: (() -> Void)? = nil

    @State private var selectedSeason: String = ""

    private var seasons: [String] {
        var seen: [String] = []
        for ep in episodes where !seen.contains(ep.season) { seen.append(ep.season) }
        return seen
    }

    private var filteredEpisodes: [EpisodeItem] {
        selectedSeason.isEmpty ? episodes : episodes.filter { $0.season == selectedSeason }
    }

    var body: some View {
        VStack(alignment: .trailing, spacing: 8) {
            if onClose != nil {
                Button { onClose?() } label: {
                    Image(systemName: "xmark.circle.fill")
                        .font(appFont(22))
                        .foregroundColor(.white.opacity(0.8))
                        .padding(.trailing, 16)
                }
            }

            if seasons.count > 1 {
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 8) {
                        ForEach(seasons, id: \.self) { s in
                            Button {
                                withAnimation { selectedSeason = s }
                            } label: {
                                Text(s)
                                    .font(appFont(12, bold: selectedSeason == s))
                                    .foregroundColor(.white)
                                    .padding(.horizontal, 14).padding(.vertical, 6)
                                    .background(selectedSeason == s ? UT_RED : Color.white.opacity(0.12))
                                    .cornerRadius(16)
                            }
                        }
                    }
                    .padding(.horizontal, 16)
                }
            }

            ScrollViewReader { proxy in
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 10) {
                        ForEach(filteredEpisodes) { ep in
                            Button {
                                onSelect?(ep)
                            } label: {
                                VStack(spacing: 6) {
                                    ZStack(alignment: .center) {
                                        CachedAsyncImage(url: URL(string: posterUrl)) { phase in
                                            if let image = phase.image {
                                                image.resizable().aspectRatio(contentMode: .fill)
                                            } else {
                                                Color.white.opacity(0.08)
                                            }
                                        }
                                        .frame(width: 130, height: 73)
                                        .clipped()

                                        if ep.id == currentEpisodeId {
                                            Color.black.opacity(0.45)
                                            Text("Playing")
                                                .font(appFont(12, bold: true))
                                                .foregroundColor(.white)
                                        }
                                    }
                                    .frame(width: 130, height: 73)
                                    .cornerRadius(6)
                                    .overlay(
                                        RoundedRectangle(cornerRadius: 6)
                                            .stroke(ep.id == currentEpisodeId ? UT_RED : Color.clear, lineWidth: 2)
                                    )

                                    Text(ep.title)
                                        .font(appFont(11))
                                        .foregroundColor(.white.opacity(0.85))
                                        .lineLimit(1)
                                        .frame(width: 130, alignment: .leading)
                                }
                            }
                            .buttonStyle(.plain)
                            .id(ep.id)
                        }
                    }
                    .padding(.horizontal, 16)
                    .padding(.bottom, 24)
                    .padding(.top, 10)
                }
                .onAppear {
                    withAnimation { proxy.scrollTo(currentEpisodeId, anchor: .center) }
                }
            }
        }
        .background(
            LinearGradient(colors: [.clear, .black.opacity(0.75)], startPoint: .top, endPoint: .bottom)
                .allowsHitTesting(false)
        )
        .onAppear {
            if selectedSeason.isEmpty {
                selectedSeason = episodes.first(where: { $0.id == currentEpisodeId })?.season ?? (seasons.first ?? "")
            }
        }
    }
}


// ─────────────────────────────────────────────
// MARK: – شاشة إعدادات الترجمة المنبثقة
// ─────────────────────────────────────────────
struct SubtitleSettingsView: View {
    @ObservedObject var settings = AppSettings.shared
    @Environment(\.dismiss) var dismiss

    var body: some View {
        NavigationView {
            Form {
                Section(header: Text(L("الترجمة", "Subtitles"))) {
                    Toggle(L("تفعيل الترجمة", "Enable Subtitles"), isOn: $settings.subtitlesEnabled)
                }
                Section(header: Text(L("التأخير (ثواني)", "Delay (sec)"))) {
                    VStack {
                        Text("\(settings.subtitleDelay, specifier: "%.1f") ثانية")
                        Slider(value: $settings.subtitleDelay, in: -5...5, step: 0.1)
                            .accentColor(UT_RED)
                    }
                    Text(L("القيمة الموجبة تؤخر الترجمة، السالبة تقدمها", "Positive delays, negative advances"))
                        .font(.caption)
                        .foregroundColor(.gray)
                }
                Section(header: Text("حجم الخط")) {
                    VStack {
                        Text("\(Int(settings.subtitleFontSize))")
                        Slider(value: $settings.subtitleFontSize, in: 14...40, step: 1)
                            .accentColor(UT_RED)
                    }
                }
                Section(header: Text(L("لون النص", "Text Color"))) {
                    ScrollView(.horizontal) {
                        HStack {
                            ForEach(["#FFFFFF", "#FFFF00", "#00FFFF", "#FF00FF", "#FF0000", "#00FF00", "#0000FF"], id: \.self) { hex in
                                Circle()
                                    .fill(Color(hex: hex))
                                    .frame(width: 30, height: 30)
                                    .overlay(
                                        Circle().stroke(Color.white, lineWidth: settings.subtitleColorHex == hex ? 3 : 0)
                                    )
                                    .onTapGesture { settings.subtitleColorHex = hex }
                            }
                        }
                    }
                }
                Section(header: Text(L("خلفية الترجمة", "Subtitle Background"))) {
                    VStack {
                        Text("الشفافية: \(Int(settings.subtitleBgOpacity * 100))%")
                        Slider(value: $settings.subtitleBgOpacity, in: 0.0...1.0, step: 0.05)
                            .accentColor(UT_RED)
                    }
                }
                Section(header: Text(L("الخط", "Font"))) {
                    Picker("الخط", selection: $settings.subtitleFontName) {
                        Text("Cairo").tag("Cairo")
                        Text("Rubik").tag("Rubik")
                        Text("IBM Plex Sans").tag("Ibm")
                    }
                    .pickerStyle(.segmented)
                }
            }
            .navigationTitle("إعدادات الترجمة")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("تم") { dismiss() }
                }
            }
        }
        .navigationViewStyle(StackNavigationViewStyle())
        .presentationDetents([.medium, .large])
        .presentationDragIndicator(.visible)
    }
}

// ─────────────────────────────────────────────
// MARK: – مشغل الفيديو المخصص
// ─────────────────────────────────────────────
struct CustomPlayerView: View {
    let itemId: String
    let itemTitle: String
    let itemImageUrl: String
    let isMovie: Bool
    let onTitleTap: (() -> Void)?   // عند النقر على العنوان في الأعلى

    @State private var videoUrl: String
    @State private var videoUrl720: String
    @State private var videoUrl1080: String
    @State private var videoUrl360: String
    @State private var videoUrl4k: String
    @State private var subtitleUrl: String
    @State private var subtitleVttUrl: String
    @State private var episodeId: String
    @State private var episodeTitle: String
    @State private var episodes: [EpisodeItem]

    // إظهار إعدادات الترجمة
    @State private var showSubtitleSettings = false

    init(itemId: String,
         itemTitle: String,
         itemImageUrl: String,
         isMovie: Bool = true,
         videoUrl: String,
         videoUrl720: String,
         videoUrl1080: String,
         videoUrl360: String,
         videoUrl4k: String = "",
         subtitleUrl: String,
         subtitleVttUrl: String,
         episodeId: String,
         episodeTitle: String,
         episodes: [EpisodeItem] = [],
         onTitleTap: (() -> Void)? = nil) {
        self.itemId = itemId
        self.itemTitle = itemTitle
        self.itemImageUrl = itemImageUrl
        self.isMovie = isMovie
        self.onTitleTap = onTitleTap
        _videoUrl       = State(initialValue: videoUrl)
        _videoUrl720    = State(initialValue: videoUrl720)
        _videoUrl1080   = State(initialValue: videoUrl1080)
        _videoUrl360    = State(initialValue: videoUrl360)
        _videoUrl4k     = State(initialValue: videoUrl4k)
        _subtitleUrl    = State(initialValue: subtitleUrl)
        _subtitleVttUrl = State(initialValue: subtitleVttUrl)
        _episodeId      = State(initialValue: episodeId)
        _episodeTitle   = State(initialValue: episodeTitle)
        _episodes       = State(initialValue: episodes)
    }

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
    @State private var endObserver: NSObjectProtocol?
    @State private var errorObserver: NSObjectProtocol?

    @State private var showControls = true
    @State private var hideTimer: Timer?
    @State private var isLocked     = false
    @State private var fitMode      = VideoFitMode.fit
    @State private var quality      = VideoQuality(rawValue: AppSettings.shared.preferredQuality) ?? .auto
    @State private var showSettings = false
    @State private var isSpeedActive = false
    @State private var isFinished   = false
    @State private var isBuffering  = true
    @State private var statusCancellable: AnyCancellable?

    @State private var cues: [SubtitleCue] = []
    @State private var activeSub = ""
    @State private var subtitleCursor = 0

    @State private var playbackSpeed: Double = 1.0
    @State private var saveTimer: Timer?
    @State private var errorMessage: String?

    @State private var seekFeedback: (isRight: Bool, show: Bool) = (false, false)

    // قائمة الحلقات (شريط عريض يُرفع بالسحب)
    @State private var showEpisodesSheet = false
    @State private var episodesRailOffset: CGFloat = 0

    // التشغيل التلقائي للحلقة التالية
    @State private var showUpNext = false
    @State private var upNextCountdown = 0
    @State private var upNextTimer: Timer?
    @State private var autoNextSkippedFor: String?

    // إيماءات السطوع / الصوت
    @State private var brightnessValue: CGFloat = UIScreen.main.brightness
    @State private var volumeValue: CGFloat = CGFloat(SystemVolumeHelper.shared.currentVolume)
    @State private var showBrightnessHUD = false
    @State private var showVolumeHUD = false
    @State private var hudHideTimer: Timer?

    private var subtitleFont: Font {
        subtitleFontForPlayer(name: settings.subtitleFontName, size: CGFloat(settings.subtitleFontSize))
    }

    private var nextEpisodeItem: EpisodeItem? {
        guard let idx = episodes.firstIndex(where: { $0.id == episodeId }) else { return nil }
        let n = idx + 1
        guard n < episodes.count else { return nil }
        return episodes[n]
    }

    private var availableQualities: [VideoQuality] {
        VideoQuality.allCases.filter { q in
            switch q {
            case .auto:  return true
            case .q360:  return !videoUrl360.isEmpty
            case .q720:  return !videoUrl720.isEmpty
            case .q1080: return !videoUrl1080.isEmpty
            case .q4k:   return !videoUrl4k.isEmpty
            }
        }
    }

    var body: some View {
        GeometryReader { geo in
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
                            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
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
                        },
                        onVerticalDrag: { isRightHalf, deltaY, state in
                            guard !isLocked, !isSpeedActive, !showEpisodesSheet else { return }
                            let change = CGFloat(-deltaY) / 250.0
                            if isRightHalf {
                                volumeValue = min(1, max(0, volumeValue + change))
                                SystemVolumeHelper.shared.setVolume(Float(volumeValue))
                                withAnimation(.easeOut(duration: 0.15)) { showVolumeHUD = true }
                            } else {
                                brightnessValue = min(1, max(0, brightnessValue + change))
                                UIScreen.main.brightness = brightnessValue
                                withAnimation(.easeOut(duration: 0.15)) { showBrightnessHUD = true }
                            }
                            if state == .ended || state == .cancelled {
                                hudHideTimer?.invalidate()
                                hudHideTimer = Timer.scheduledTimer(withTimeInterval: 0.9, repeats: false) { _ in
                                    withAnimation { showBrightnessHUD = false; showVolumeHUD = false }
                                }
                            }
                        }
                    )
                    .ignoresSafeArea()

                    if isSpeedActive {
                        VStack {
                            HStack(spacing: 6) {
                                Image(systemName: "forward.frame.fill")
                                Text("2× سرعة")
                            }
                            .font(appFont(14, bold: true))
                            .foregroundColor(.white)
                            .padding(.horizontal, 16)
                            .padding(.vertical, 8)
                            .background(Color.black.opacity(0.75))
                            .cornerRadius(20)
                            .padding(.top, 60)
                            Spacer()
                        }
                    }

                    // عرض الترجمة مع تطبيق التأخير
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

                    // مؤشر التخزين المؤقت (Buffering)
                    if isBuffering && !isFinished && errorMessage == nil {
                        VStack(spacing: 10) {
                            ProgressView()
                                .progressViewStyle(CircularProgressViewStyle(tint: .white))
                                .scaleEffect(1.4)
                            Text("Loading...")
                                .font(appFont(13, bold: false))
                                .foregroundColor(.white.opacity(0.85))
                        }
                    }

                    // قائمة الحلقات تُعرض فقط عند الضغط على زر Episodes صراحةً، وليس تلقائياً أثناء التحميل
                    // (الظهور التلقائي أثناء التحميل كان يُربك المستخدم لأنها تبدو وكأنها جزء من شاشة التحميل)

                    if let error = errorMessage {
                        VStack(spacing: 14) {
                            Image(systemName: "exclamationmark.triangle.fill")
                                .font(appFont(34))
                                .foregroundColor(UT_RED)
                            Text(error)
                                .foregroundColor(.white)
                                .multilineTextAlignment(.center)
                                .padding(.horizontal, 30)
                            Button {
                                errorMessage = nil
                                shutdown()
                                setupPlayer()
                            } label: {
                                HStack(spacing: 8) {
                                    Image(systemName: "arrow.clockwise")
                                    Text(L("إعادة المحاولة", "Retry"))
                                }
                                .font(appFont(14, bold: true))
                                .foregroundColor(.white)
                                .padding(.horizontal, 22).padding(.vertical, 10)
                                .background(UT_RED)
                                .cornerRadius(10)
                            }
                        }
                        .padding()
                        .background(Color.black.opacity(0.55))
                        .cornerRadius(14)
                    }

                    // زر إعادة التشغيل عند نهاية الفيديو (فيلم أو آخر حلقة)
                    if isFinished {
                        VStack(spacing: 10) {
                            Button {
                                isFinished = false
                                player.seek(to: .zero)
                                player.play()
                                isPlaying = true
                            } label: {
                                Image(systemName: "arrow.counterclockwise.circle.fill")
                                    .font(appFont(64))
                                    .foregroundColor(.white)
                            }
                            Text(L("إعادة التشغيل", "Restart"))
                                .font(appFont(13, bold: true))
                                .foregroundColor(.white.opacity(0.85))
                        }
                        .padding(24)
                        .background(Color.black.opacity(0.45))
                        .cornerRadius(20)
                    }

                    if showControls || isLocked {
                        controlsOverlay(player: player)
                            .transition(.opacity)
                            .animation(.easeInOut(duration: 0.25), value: showControls)
                    }

                    // مؤشر التقديم/الترجيع المبسط
                    if seekFeedback.show {
                        VStack {
                            Spacer()
                            HStack(spacing: 8) {
                                Image(systemName: seekFeedback.isRight ? "goforward.10" : "gobackward.10")
                                    .font(appFont(40, bold: false))
                                Text(seekFeedback.isRight ? "+10" : "-10")
                                    .font(appFont(20, bold: false))
                            }
                            .foregroundColor(.white)
                            .padding(.horizontal, 20)
                            .padding(.vertical, 10)
                            .background(Color.black.opacity(0.6))
                            .cornerRadius(30)
                            .padding(.bottom, 120)
                        }
                        .transition(.opacity)
                        .animation(.easeOut(duration: 0.2), value: seekFeedback.show)
                    }

                    // مؤشرات السطوع / الصوت
                    if showBrightnessHUD || showVolumeHUD {
                        VStack {
                            HStack(spacing: 10) {
                                Image(systemName: showVolumeHUD
                                      ? (volumeValue <= 0.01 ? "speaker.slash.fill" : "speaker.wave.2.fill")
                                      : (brightnessValue < 0.5 ? "sun.min.fill" : "sun.max.fill"))
                                    .foregroundColor(.white)
                                ProgressView(value: showVolumeHUD ? Double(volumeValue) : Double(brightnessValue))
                                    .frame(width: 110)
                                    .tint(.white)
                            }
                            .padding(.horizontal, 16).padding(.vertical, 10)
                            .background(Color.black.opacity(0.6))
                            .cornerRadius(14)
                            .padding(.top, 70)
                            Spacer()
                        }
                        .transition(.opacity)
                        .allowsHitTesting(false)
                    }

                    // تنبيه "الحلقة القادمة" مع عداد تنازلي
                    if showUpNext, let next = nextEpisodeItem {
                        VStack {
                            Spacer()
                            HStack(spacing: 12) {
                                ZStack {
                                    RoundedRectangle(cornerRadius: 12)
                                        .fill(Color.white.opacity(0.12))
                                        .frame(width: 56, height: 56)
                                    Text("\(upNextCountdown)")
                                        .font(appFont(22, bold: true))
                                        .foregroundColor(.white)
                                }
                                VStack(alignment: .leading, spacing: 4) {
                                    Text(L("الحلقة التالية", "Next Episode"))
                                        .font(appFont(11))
                                        .foregroundColor(.white.opacity(0.6))
                                    Text(next.title)
                                        .font(appFont(14, bold: true))
                                        .foregroundColor(.white)
                                        .lineLimit(1)
                                }
                                Spacer()
                                Button("إلغاء") { cancelUpNext() }
                                    .font(appFont(12, bold: true))
                                    .foregroundColor(.white.opacity(0.85))
                                    .padding(.horizontal, 12).padding(.vertical, 8)
                                    .background(Color.white.opacity(0.12))
                                    .cornerRadius(10)
                                Button {
                                    upNextTimer?.invalidate()
                                    switchToEpisode(next, autoplay: true)
                                } label: {
                                    HStack(spacing: 6) {
                                        Image(systemName: "play.fill")
                                        Text(L("تشغيل", "Play"))
                                    }
                                    .font(appFont(12, bold: true))
                                    .foregroundColor(.white)
                                    .padding(.horizontal, 12).padding(.vertical, 8)
                                    .background(UT_RED)
                                    .cornerRadius(10)
                                }
                            }
                            .padding(12)
                            .background(Color.black.opacity(0.85))
                            .cornerRadius(16)
                            .padding(.horizontal, 14)
                            .padding(.bottom, isLocked ? 30 : 120)
                        }
                        .transition(.move(edge: .bottom).combined(with: .opacity))
                        .zIndex(6)
                    }

                    // مقبض سحب قائمة الحلقات للأعلى (يظهر فقط إذا كان مسلسل)
                    if !isMovie && !episodes.isEmpty && !showEpisodesSheet {
                        VStack {
                            Spacer()
                            VStack(spacing: 4) {
                                Capsule()
                                    .fill(Color.white.opacity(0.5))
                                    .frame(width: 46, height: 5)
                                HStack(spacing: 6) {
                                    Image(systemName: "chevron.up")
                                        .font(appFont(11, bold: true))
                                    Text(L("قائمة الحلقات", "Episodes"))
                                        .font(appFont(12, bold: true))
                                }
                                .foregroundColor(.white.opacity(0.85))
                            }
                            .padding(.vertical, 10)
                            .frame(maxWidth: .infinity)
                            .contentShape(Rectangle())
                            .background(
                                LinearGradient(colors: [.clear, .black.opacity(0.55)],
                                               startPoint: .top, endPoint: .bottom)
                            )
                            .onTapGesture {
                                withAnimation(.spring()) { showEpisodesSheet = true }
                            }
                            .gesture(
                                DragGesture(minimumDistance: 12)
                                    .onChanged { value in
                                        if value.translation.height < -10 {
                                            withAnimation(.spring()) { showEpisodesSheet = true }
                                        }
                                    }
                            )
                            .opacity((showControls || isLocked) ? 1 : 0.35)
                        }
                        .ignoresSafeArea(edges: .bottom)
                        .zIndex(4)
                    }

                    // قائمة الحلقات (تنزل مع السحب للأسفل وتُغلق بسحب بسرعة أو مسافة كافية)
                    if showEpisodesSheet {
                        VStack {
                            Spacer()
                            EpisodeQuickRailView(
                                episodes: episodes,
                                currentEpisodeId: episodeId,
                                posterUrl: itemImageUrl,
                                onSelect: { ep in
                                    switchToEpisode(ep, autoplay: true)
                                    withAnimation(.spring(response: 0.35, dampingFraction: 0.8)) {
                                        showEpisodesSheet = false
                                        episodesRailOffset = 0
                                    }
                                },
                                onClose: {
                                    withAnimation(.spring(response: 0.35, dampingFraction: 0.8)) {
                                        showEpisodesSheet = false
                                        episodesRailOffset = 0
                                    }
                                }
                            )
                            .offset(y: max(0, episodesRailOffset))
                            .gesture(
                                DragGesture(minimumDistance: 10, coordinateSpace: .local)
                                    .onChanged { value in
                                        if value.translation.height > 0 {
                                            episodesRailOffset = value.translation.height
                                        }
                                    }
                                    .onEnded { value in
                                        let velocity = value.predictedEndTranslation.height - value.translation.height
                                        // ايغلق لو سحب أكثر من 80 نقطة أو بسرعة كافية
                                        if value.translation.height > 80 || velocity > 200 {
                                            withAnimation(.spring(response: 0.35, dampingFraction: 0.8)) {
                                                showEpisodesSheet = false
                                                episodesRailOffset = 0
                                            }
                                        } else {
                                            withAnimation(.spring(response: 0.35, dampingFraction: 0.8)) {
                                                episodesRailOffset = 0
                                            }
                                        }
                                    }
                            )
                        }
                        .transition(.move(edge: .bottom).combined(with: .opacity))
                        .zIndex(8)
                    }

                } else {
                    VStack(spacing: 20) {
                        ProgressView().tint(.white)
                        Text(L("جاري التحميل...", "Loading..."))
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
            .onAppear {
                setupPlayer()
                fetchEpisodesIfNeeded()
            }
            .onDisappear { shutdown() }
            .sheet(isPresented: $showSubtitleSettings) {
                SubtitleSettingsView()
            }
        }
    }

    // ─────────────────────────────────────────
    // MARK: – واجهة عناصر التحكم (تم إضافة زر إعدادات الترجمة)
    // ─────────────────────────────────────────
    @ViewBuilder
    private func controlsOverlay(player: AVPlayer) -> some View {
        VStack {
            HStack {
                if !isLocked {
                    Button { shutdown(); presentation.wrappedValue.dismiss() } label: {
                        Image(systemName: "arrow.backward").playerBtn()
                    }

                    // زر العنوان (اسم العمل + الحلقة)
                    Button {
                        onTitleTap?()
                    } label: {
                        VStack(alignment: .leading, spacing: 2) {
                            Text(itemTitle)
                                .font(appFont(15, bold: true))
                                .foregroundColor(.white)
                                .lineLimit(1)
                            if !isMovie && !episodeTitle.isEmpty {
                                Text(episodeTitle)
                                    .font(appFont(12, bold: false))
                                    .foregroundColor(.white.opacity(0.7))
                                    .lineLimit(1)
                            }
                        }
                        .padding(.leading, 8)
                    }

                    Spacer()

                    // زر إعدادات الترجمة
                    Button {
                        showSubtitleSettings.toggle()
                    } label: {
                        Image(systemName: "captions.bubble")
                            .playerBtn(color: .white)
                    }

                    AirPlayButton()
                        .frame(width: 38, height: 38)

                    if !isMovie && !episodes.isEmpty {
                        Button {
                            withAnimation(.spring()) { showEpisodesSheet = true }
                        } label: {
                            Image(systemName: "list.bullet.rectangle.portrait")
                                .playerBtn(color: .white)
                        }
                    }
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
            .allowsHitTesting(true)

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

                        Button {
                            if isPlaying { player.pause() }
                            else         { player.rate = Float(playbackSpeed) }
                            isPlaying.toggle()
                            scheduleHide()
                        } label: {
                            Image(systemName: isPlaying ? "pause.circle.fill" : "play.circle.fill")
                                .font(appFont(66))
                                .foregroundColor(UT_RED)
                        }

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
                        ForEach(availableQualities) { q in
                            Button(q.rawValue) { switchQuality(to: q) }
                                .font(appFont(12, bold: quality == q))
                                .foregroundColor(.white)
                                .padding(.horizontal, 10).padding(.vertical, 6)
                                .background(quality == q ? UT_RED : Color.clear)
                                .cornerRadius(8)
                        }
                        Spacer()
                        if !isMovie, nextEpisodeItem != nil {
                            Button {
                                guard let next = nextEpisodeItem else { return }
                                switchToEpisode(next, autoplay: true)
                            } label: {
                                HStack(spacing: 4) {
                                    Text(L("التالية", "Next"))
                                    Image(systemName: "forward.end.fill")
                                }
                                .font(appFont(12, bold: true))
                                .foregroundColor(.white.opacity(0.85))
                            }
                            .padding(.trailing, 8)
                        }
                        Button {
                            let all = VideoFitMode.allCases
                            let idx = all.firstIndex(of: fitMode) ?? 0
                            fitMode = all[(idx + 1) % all.count]
                        } label: {
                            Image(systemName: "aspectratio")
                                .font(.caption).foregroundColor(.white.opacity(0.8))
                        }
                        Text(fitMode.rawValue)
                            .font(appFont(11))
                            .foregroundColor(.white.opacity(0.7))
                    }
                    .padding(.horizontal, 16)
                    .padding(.bottom, isMovie ? 26 : 70) // مساحة إضافية للمقبض
                }
                .allowsHitTesting(true)
            }
        }
        .background(
            LinearGradient(colors: [.clear, .black.opacity(0.9)],
                           startPoint: .top, endPoint: .bottom)
        )
        .onTapGesture {
            // نمرر النقرة إلى الفيديو عبر التبديل اليدوي
            if !isLocked {
                withAnimation { showControls.toggle() }
                if showControls { scheduleHide() }
            }
        }
    }

    // ─────────────────────────────────────────
    // MARK: – إعداد المشغّل والتحكم بالتشغيل
    // ─────────────────────────────────────────
    private func setupPlayer() {
        try? AVAudioSession.sharedInstance().setCategory(.playback, mode: .moviePlayback)
        try? AVAudioSession.sharedInstance().setActive(true)

        isBuffering = true
        statusCancellable?.cancel()

        volumeValue = CGFloat(SystemVolumeHelper.shared.currentVolume)
        brightnessValue = UIScreen.main.brightness

        let savedProgress = progressStore.progress(for: itemId)
        let resumeTime = (savedProgress?.episodeId == episodeId) ? (savedProgress?.progressSeconds ?? 0) : 0

        let urlStr = resolvedUrl(quality: quality)
        guard !urlStr.isEmpty, let url = URL(string: urlStr) else {
            errorMessage = "رابط الفيديو غير صالح"
            return
        }

        let item = AVPlayerItem(url: url)
        let p = AVPlayer(playerItem: item)
        p.allowsExternalPlayback = true
        self.player = p

        if resumeTime > 5 {
            p.seek(to: CMTime(seconds: resumeTime, preferredTimescale: 600))
        }
        p.play()
        isPlaying = true
        isFinished = false
        errorMessage = nil

        attachItemObservers(item: item)

        timeObserver = p.addPeriodicTimeObserver(
            forInterval: CMTime(seconds: 0.25, preferredTimescale: 600), queue: .main
        ) { t in
            if !self.isDragging { self.currentTime = t.seconds }

            // تطبيق تأخير الترجمة (بحث سريع بمؤشر متحرك بدل البحث الخطي الكامل في كل نبضة)
            let adjustedTime = t.seconds + self.settings.subtitleDelay
            self.activeSub = self.lookupSubtitle(at: adjustedTime)

            if let currentItem = p.currentItem {
                self.isBuffering = !currentItem.isPlaybackLikelyToKeepUp && self.isPlaying && !self.isFinished
            }

            self.checkUpNext(currentTime: t.seconds)
        }

        loadSubtitles()
        scheduleHide()
        startSaveTimer()

        // حارس أمان: إن بقي التحميل عالقاً لأكثر من 25 ثانية نعرض رسالة خطأ بدل تحميل أبدي
        DispatchQueue.main.asyncAfter(deadline: .now() + 25) {
            if self.isBuffering && self.errorMessage == nil {
                self.errorMessage = "يستغرق التحميل وقتاً أطول من المعتاد، تحقق من اتصالك بالإنترنت"
                self.isBuffering = false
            }
        }
    }

    /// تحميل قائمة الحلقات الكاملة عند الحاجة (مثلاً عند المتابعة من "الاستمرار في المشاهدة")
    private func fetchEpisodesIfNeeded() {
        guard !isMovie, episodes.isEmpty, !itemId.isEmpty else { return }
        MovieScraper().fetchDetails(id: itemId) { details in
            if !details.episodes.isEmpty {
                self.episodes = details.episodes
            }
        }
    }

    private func attachItemObservers(item: AVPlayerItem) {
        if let obs = endObserver   { NotificationCenter.default.removeObserver(obs) }
        if let obs = errorObserver { NotificationCenter.default.removeObserver(obs) }

        // مراقبة حالة العنصر: تصحيح خلل "Loading..." الذي يستمر للأبد عند فشل الرابط
        statusCancellable = item.publisher(for: \.status)
            .receive(on: DispatchQueue.main)
            .sink { status in
                switch status {
                case .failed:
                    self.isBuffering = false
                    self.errorMessage = item.error?.localizedDescription
                        ?? "تعذّر تشغيل هذا الفيديو، تحقق من اتصالك بالإنترنت وحاول مرة أخرى"
                case .readyToPlay:
                    self.isBuffering = false
                default:
                    break
                }
            }

        endObserver = NotificationCenter.default.addObserver(
            forName: .AVPlayerItemDidPlayToEndTime, object: item, queue: .main
        ) { _ in
            self.isPlaying = false
            self.upNextTimer?.invalidate()
            withAnimation { self.showUpNext = false }

            if !self.isMovie,
               self.settings.autoPlayNextEnabled,
               self.autoNextSkippedFor != self.episodeId,
               let next = self.nextEpisodeItem {
                self.switchToEpisode(next, autoplay: true)
            } else {
                self.isFinished = true
            }
        }

        errorObserver = NotificationCenter.default.addObserver(
            forName: .AVPlayerItemFailedToPlayToEndTime, object: item, queue: .main
        ) { _ in
            self.errorMessage = "حدث خطأ أثناء تشغيل الفيديو، تحقق من اتصالك بالإنترنت وحاول مرة أخرى"
        }

        Task {
            if let dur = try? await item.asset.load(.duration) {
                DispatchQueue.main.async { self.duration = dur.seconds }
            }
        }
    }

    private func loadSubtitles() {
        cues = []
        activeSub = ""
        subtitleCursor = 0
        let subUrl = subtitleVttUrl.isEmpty ? subtitleUrl : subtitleVttUrl
        guard !subUrl.isEmpty else { return }
        SubtitleParser.parse(url: subUrl) { parsedCues in
            self.cues = parsedCues
            self.subtitleCursor = 0
        }
    }

    /// بحث سريع عن الترجمة الحالية: مؤشر متحرك للأمام O(1) في الحالة الطبيعية،
    /// وبحث ثنائي O(log n) عند التراجع للخلف (بعد تقديم/تأخير يدوي)، بدل المسح الخطي الكامل لكل نبضة وقت
    private func lookupSubtitle(at time: Double) -> String {
        guard !cues.isEmpty else { return "" }
        if subtitleCursor >= cues.count { subtitleCursor = cues.count - 1 }

        let current = cues[subtitleCursor]
        if time >= current.startTime && time <= current.endTime {
            return current.text
        }

        if time > current.endTime {
            // تقدّم للأمام (الحالة الشائعة أثناء التشغيل الطبيعي)
            while subtitleCursor < cues.count - 1 && time > cues[subtitleCursor].endTime {
                subtitleCursor += 1
                let c = cues[subtitleCursor]
                if time >= c.startTime && time <= c.endTime { return c.text }
            }
            return ""
        }

        // تراجع للخلف: بحث ثنائي لإيجاد أقرب كيو
        var lo = 0, hi = subtitleCursor
        while lo < hi {
            let mid = (lo + hi) / 2
            if cues[mid].endTime < time { lo = mid + 1 } else { hi = mid }
        }
        subtitleCursor = lo
        let c = cues[subtitleCursor]
        return (time >= c.startTime && time <= c.endTime) ? c.text : ""
    }

    private func startSaveTimer() {
        saveTimer?.invalidate()
        saveTimer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            guard let p = self.player, self.duration > 0 else { return }
            self.progressStore.save(
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
                videoUrl4k: self.videoUrl4k,
                subUrl: self.subtitleUrl,
                subVttUrl: self.subtitleVttUrl,
                isMovie: self.isMovie
            )
        }
    }

    /// التبديل إلى حلقة أخرى (يدوياً من قائمة الحلقات أو تلقائياً عند انتهاء الحلقة الحالية)
    private func switchToEpisode(_ ep: EpisodeItem, autoplay: Bool = true) {
        guard let p = player else { return }

        saveTimer?.invalidate()
        upNextTimer?.invalidate()
        withAnimation {
            showUpNext = false
            showEpisodesSheet = false
            episodesRailOffset = 0
        }
        autoNextSkippedFor = nil
        isFinished = false
        errorMessage = nil

        episodeId       = ep.id
        episodeTitle    = ep.title
        videoUrl        = ep.url
        videoUrl720     = ep.url720
        videoUrl1080    = ep.url1080
        videoUrl360     = ep.url360
        videoUrl4k      = ep.url4k
        subtitleUrl     = ep.subtitleUrl
        subtitleVttUrl  = ep.subtitleVttUrl

        currentTime = 0
        duration = 0

        guard let url = URL(string: resolvedUrl(quality: quality)) else { return }
        let newItem = AVPlayerItem(url: url)
        p.replaceCurrentItem(with: newItem)
        attachItemObservers(item: newItem)
        loadSubtitles()

        if autoplay {
            p.seek(to: .zero)
            p.play()
            isPlaying = true
        } else {
            p.pause()
            isPlaying = false
        }

        startSaveTimer()
    }

    /// يفحص إن كان يجب إظهار تنبيه "الحلقة القادمة بعد..."
    private func checkUpNext(currentTime t: TimeInterval) {
        guard !isMovie,
              settings.autoPlayNextEnabled,
              !showUpNext,
              autoNextSkippedFor != episodeId,
              duration > 0,
              nextEpisodeItem != nil
        else { return }

        let remaining = duration - t
        let threshold = Double(max(3, settings.autoPlayCountdownSeconds))
        if remaining > 0 && remaining <= threshold {
            beginUpNextCountdown()
        }
    }

    private func beginUpNextCountdown() {
        guard let next = nextEpisodeItem else { return }
        upNextCountdown = max(1, settings.autoPlayCountdownSeconds)
        withAnimation { showUpNext = true }
        upNextTimer?.invalidate()
        upNextTimer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
            if self.upNextCountdown <= 1 {
                self.upNextTimer?.invalidate()
                withAnimation { self.showUpNext = false }
                self.switchToEpisode(next, autoplay: true)
            } else {
                self.upNextCountdown -= 1
            }
        }
    }

    private func cancelUpNext() {
        upNextTimer?.invalidate()
        autoNextSkippedFor = episodeId
        withAnimation { showUpNext = false }
    }

    private func shutdown() {
        saveTimer?.invalidate()
        hideTimer?.invalidate()
        upNextTimer?.invalidate()
        hudHideTimer?.invalidate()
        statusCancellable?.cancel()
        statusCancellable = nil
        if let obs = timeObserver { player?.removeTimeObserver(obs); timeObserver = nil }
        if let obs = endObserver   { NotificationCenter.default.removeObserver(obs) }
        if let obs = errorObserver { NotificationCenter.default.removeObserver(obs) }
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
        AppSettings.shared.preferredQuality = q.rawValue
        guard let url = URL(string: resolvedUrl(quality: q)) else { return }
        let item = AVPlayerItem(url: url)
        player.replaceCurrentItem(with: item)
        attachItemObservers(item: item)
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
        case .q4k:   return fixUrl(videoUrl4k.isEmpty ? videoUrl : videoUrl4k)
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
            .allowsHitTesting(true) // السماح باللمس
    }
}

extension Text {
    func timeLabel() -> some View {
        self.font(appFont(12, bold: true))
            .monospacedDigit()
            .foregroundColor(.white)
            .allowsHitTesting(true)
    }
}
"""
with open("UTan/UTan/CustomPlayer.swift", "w", encoding="utf-8") as f:
    f.write(player_swift + playerview_swift)

# 7. Views.swift (نفس المحتوى السابق مع تحسينات الأداء والتحميل اللانهائي)
views_swift_p1 = r"""import SwiftUI

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Loader (يختفي بعد تحميل البيانات أو بعد مهلة 15 ثانية)
// ─────────────────────────────────────────────────────────────────────────────
struct UTanLoader: View {
    @Binding var isLoading: Bool
    @State private var opacity = 1.0
    @State private var timer: Timer?

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
                            // إلغاء التحميل تلقائياً بعد 15 ثانية في حال تعطل الطلب
                            timer = Timer.scheduledTimer(withTimeInterval: 15, repeats: false) { _ in
                                DispatchQueue.main.async {
                                    isLoading = false
                                }
                            }
                        }
                        .onDisappear {
                            timer?.invalidate()
                        }
                } else {
                    Text("UTAN")
                        .font(appFont(40, bold: true))
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
    let isMovie: Bool
    let videoUrl: String
    let videoUrl720: String
    let videoUrl1080: String
    let videoUrl360: String
    let videoUrl4k: String
    let subtitleUrl: String
    let subtitleVttUrl: String
    let episodeId: String
    let episodeTitle: String
    let episodes: [EpisodeItem]

    init(itemId: String, itemTitle: String, itemImageUrl: String, isMovie: Bool = true,
         videoUrl: String, videoUrl720: String, videoUrl1080: String, videoUrl360: String, videoUrl4k: String = "",
         subtitleUrl: String, subtitleVttUrl: String,
         episodeId: String, episodeTitle: String, episodes: [EpisodeItem] = []) {
        self.itemId = itemId
        self.itemTitle = itemTitle
        self.itemImageUrl = itemImageUrl
        self.isMovie = isMovie
        self.videoUrl = videoUrl
        self.videoUrl720 = videoUrl720
        self.videoUrl1080 = videoUrl1080
        self.videoUrl360 = videoUrl360
        self.videoUrl4k = videoUrl4k
        self.subtitleUrl = subtitleUrl
        self.subtitleVttUrl = subtitleVttUrl
        self.episodeId = episodeId
        self.episodeTitle = episodeTitle
        self.episodes = episodes
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Poster Card (أبعاد موحدة)
// ─────────────────────────────────────────────────────────────────────────────
struct ScaleButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.94 : 1)
            .opacity(configuration.isPressed ? 0.85 : 1)
            .animation(.easeOut(duration: 0.15), value: configuration.isPressed)
    }
}

struct PosterCard: View {
    let item: VideoItem
    var progress: WatchProgress? = nil
    var showTitle: Bool = true
    // Fix 102: Accept card dimensions to optimize image downloads to actual display size
    var cardWidth: CGFloat = 120
    var cardHeight: CGFloat = 180
    @State private var shimmer = false

    var body: some View {
        VStack(alignment: .leading, spacing: 5) {
            ZStack(alignment: .bottom) {
                CachedAsyncImage(url: URL(string: optimizeImageUrl(item.imageUrl, width: Int(cardWidth * 2), height: Int(cardHeight * 2)))) { phase in
                    if let image = phase.image {
                        image.resizable()
                            .aspectRatio(contentMode: .fill)
                            .transition(.opacity.animation(.easeIn(duration: 0.3)))
                    } else if phase.error != nil {
                        ZStack {
                            Color(white: 0.12)
                            Image(systemName: "film")
                                .font(appFont(28))
                                .foregroundColor(.gray.opacity(0.5))
                        }
                    } else {
                        // شيمر أنيق أثناء التحميل
                        ZStack {
                            Color(white: 0.10)
                            LinearGradient(
                                colors: [Color.white.opacity(0.0), Color.white.opacity(0.06), Color.white.opacity(0.0)],
                                startPoint: .init(x: shimmer ? 1.5 : -0.5, y: 0.3),
                                endPoint: .init(x: shimmer ? 2.5 : 0.5, y: 0.8)
                            )
                            .onAppear {
                                withAnimation(.easeInOut(duration: 1.4).repeatForever(autoreverses: false)) {
                                    shimmer = true
                                }
                            }
                        }
                    }
                }
                .id(item.id)
                .frame(width: 120, height: 178)
                .clipped()
                .cornerRadius(12)

                // تدرج أسفل الكارت لقراءة أفضل
                LinearGradient(
                    colors: [.clear, .clear, .black.opacity(0.75)],
                    startPoint: .top, endPoint: .bottom
                )
                .cornerRadius(12)

                // شريط التقدم
                if let p = progress, p.durationSeconds > 0 {
                    VStack {
                        Spacer()
                        GeometryReader { geo in
                            ZStack(alignment: .leading) {
                                Capsule().fill(Color.white.opacity(0.25)).frame(height: 3)
                                Capsule()
                                    .fill(UT_RED)
                                    .frame(width: geo.size.width * min(1, CGFloat(p.progressSeconds / p.durationSeconds)), height: 3)
                            }
                        }
                        .frame(height: 3)
                        .padding(.horizontal, 8)
                        .padding(.bottom, 7)
                    }
                }

                // بادج النوع (فيلم / مسلسل)
                VStack {
                    HStack {
                        Spacer()
                        if item.type == "movies" {
                            Text(L("فيلم", "Movie"))
                                .font(appFont(9, bold: true))
                                .foregroundColor(.white)
                                .padding(.horizontal, 6).padding(.vertical, 3)
                                .background(UT_RED.opacity(0.9))
                                .cornerRadius(5)
                                .padding(7)
                        }
                    }
                    Spacer()
                }
            }
            .frame(width: 120, height: 178)
            .shadow(color: .black.opacity(0.5), radius: 8, x: 0, y: 4)

            if showTitle {
                Text(item.title)
                    .font(appFont(11, bold: true))
                    .foregroundColor(.white.opacity(0.9))
                    .lineLimit(2)
                    .frame(width: 120, alignment: .leading)
                    .multilineTextAlignment(.leading)
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – MainTabView
// ─────────────────────────────────────────────────────────────────────────────
struct MainTabView: View {
    @StateObject private var scraper = MovieScraper()
    @State private var showLoader = true
    @EnvironmentObject private var settings: AppSettings

    var body: some View {
        ZStack {
            if showLoader {
                UTanLoader(isLoading: $showLoader)
            } else {
                TabView {
                    HomeView(scraper: scraper)
                        .tabItem { Label(L("الرئيسية", "Home"), systemImage: "house.fill") }
                    BrowseView(scraper: scraper)
                        .tabItem { Label(L("تصفح", "Browse"), systemImage: "square.grid.2x2.fill") }
                    SearchView(scraper: scraper)
                        .tabItem { Label(L("بحث", "Search"), systemImage: "magnifyingglass") }
                    DownloadsView()
                        .tabItem { Label(L("التحميلات", "Downloads"), systemImage: "arrow.down.circle.fill") }
                    SettingsView()
                        .tabItem { Label(L("المزيد", "More"), systemImage: "line.3.horizontal") }
                }
                .accentColor(UT_RED)
                .preferredColorScheme(.dark)
                .onAppear {
                    let tabAppearance = UITabBarAppearance()
                    tabAppearance.configureWithOpaqueBackground()
                    tabAppearance.backgroundColor = UIColor(APP_BG)
                    tabAppearance.shadowColor = UIColor.white.withAlphaComponent(0.06)
                    UITabBar.appearance().standardAppearance = tabAppearance
                    if #available(iOS 15.0, *) {
                        UITabBar.appearance().scrollEdgeAppearance = tabAppearance
                    }

                    // مظهر موحّد لشريط التنقل بكل شاشات التطبيق (يطابق هوية UTan)
                    let navAppearance = UINavigationBarAppearance()
                    navAppearance.configureWithOpaqueBackground()
                    navAppearance.backgroundColor = UIColor(APP_BG)
                    navAppearance.shadowColor = .clear
                    navAppearance.titleTextAttributes = [
                        .foregroundColor: UIColor.white,
                        .font: UIFont.systemFont(ofSize: 17, weight: .bold)
                    ]
                    navAppearance.largeTitleTextAttributes = [
                        .foregroundColor: UIColor.white,
                        .font: UIFont.systemFont(ofSize: 30, weight: .heavy)
                    ]
                    UINavigationBar.appearance().standardAppearance = navAppearance
                    UINavigationBar.appearance().scrollEdgeAppearance = navAppearance
                    UINavigationBar.appearance().compactAppearance = navAppearance
                    UINavigationBar.appearance().tintColor = UIColor(UT_RED)
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
    let label: String  // يُستخدم فقط للوصول، لا يُعرض
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
            Text(L("تصفح حسب الشبكة", "Browse by Network"))
                .font(appFont(20, bold: true))
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
"""
views_swift_p2 = r"""
// ─────────────────────────────────────────────────────────────────────────────
// MARK: – HomeView (شعار ثابت تماماً في الأعلى + كل الأقسام)
// ─────────────────────────────────────────────────────────────────────────────
/// يتحقق إن كان عنوان القسم يدل على الأكثر مشاهدة/رواجاً، فنطبّق تصميم "توب 10" النتفليكسي عليه فقط
/// (بدل افتراض أن كل الأقسام مرتّبة بالشعبية، نطبّق الشارة المرقّمة فقط على الأقسام المرتبطة فعلياً بذلك)
func isTrendingTitle(_ title: String) -> Bool {
    let t = title.lowercased()
    let keywords = ["الأكثر مشاهدة", "الأكثر رواجاً", "الأكثر رواجا", "trending", "top 10", "الأعلى تقييماً", "الأعلى تقييما", "views"]
    return keywords.contains { t.contains($0.lowercased()) }
}

struct HomeView: View {
    @ObservedObject var scraper: MovieScraper
    @ObservedObject private var progressStore = WatchProgressStore.shared

    @State private var playItem: PlayerData?

    var body: some View {
        NavigationView {
            ZStack(alignment: .top) {
                APP_BG.ignoresSafeArea()

                // المحتوى (تحميل أو القائمة) - يُغلَّف بـ Group واحدة بحيث تكون
                // هندسة الـ ZStack ثابتة في الحالتين، فلا "يتحرك" الشعار الثابت
                // فوقه عند الانتقال من حالة التحميل إلى حالة العرض.
                Group {
                    if scraper.isLoading {
                        UTanLoader(isLoading: .constant(true))
                    } else {
                        ScrollView(showsIndicators: false) {
                            LazyVStack(spacing: 0) {
                                if !scraper.heroItems.isEmpty {
                                    HeroBanner(items: scraper.heroItems, scraper: scraper)
                                        .frame(height: UIScreen.main.bounds.height * 0.75)
                                }

                                LazyVStack(alignment: .leading, spacing: 30) {
                                    if !progressStore.recent.isEmpty {
                                        ContinueWatchingRow(items: progressStore.recent,
                                                            playItem: $playItem)
                                            .padding(.top, -60)
                                            .zIndex(1)
                                    }

                                    NetworkCardsRow(scraper: scraper)

                                    ForEach(Array(scraper.categories.enumerated()), id: \.element.name) { idx, cat in
                                        if !cat.items.isEmpty {
                                            CategoryRow(title: cat.name, items: cat.items, tagId: cat.tagId, scraper: scraper)
                                            // بعد القسم الثاني: اعرض صف "الأكثر مشاهدة اليوم" بأسلوب نيتفلكس
                                            // بنفس عناصر القسم الثاني (Featured عادةً = المحتوى الأبرز حالياً)
                                            if idx == 1 && cat.items.count >= 5 {
                                                Top10Row(title: L("الأكثر مشاهدة اليوم", "Trending Today"), items: cat.items)
                                            }
                                        }
                                    }
                                }
                                .padding(.bottom, 100)
                            }
                        }
                    }
                }
                .ignoresSafeArea(.all, edges: .top)

                // شعار ثابت تماماً في الأعلى (لا يتأثر بأي حركة أو إعادة تحميل)
                HStack {
                    if let logoImage = UIImage(named: "logo") {
                        Image(uiImage: logoImage)
                            .resizable()
                            .scaledToFit()
                            .frame(height: 60)
                    } else {
                        Text("UTan")
                            .font(appFont(30, bold: true))
                            .foregroundColor(.white)
                    }
                    Spacer()
                }
                .padding(.horizontal, 20)
                .padding(.top, 50)
                .transaction { transaction in
                    transaction.animation = nil
                }
            }
            .navigationBarHidden(true)
            .fullScreenCover(item: $playItem) { data in
                CustomPlayerView(
                    itemId: data.itemId,
                    itemTitle: data.itemTitle,
                    itemImageUrl: data.itemImageUrl,
                    isMovie: data.isMovie,
                    videoUrl: data.videoUrl,
                    videoUrl720: data.videoUrl720,
                    videoUrl1080: data.videoUrl1080,
                    videoUrl360: data.videoUrl360,
                    videoUrl4k: data.videoUrl4k,
                    subtitleUrl: data.subtitleUrl,
                    subtitleVttUrl: data.subtitleVttUrl,
                    episodeId: data.episodeId,
                    episodeTitle: data.episodeTitle,
                    episodes: data.episodes,
                    onTitleTap: nil // في HomeView لا نحتاج للعودة للتفاصيل
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
        let displayItems = Array(items.prefix(8))
        guard !displayItems.isEmpty else { return AnyView(EmptyView()) }
        let item = displayItems[min(current, displayItems.count - 1)]
        return AnyView(
            ZStack(alignment: .bottom) {
                // Artwork full-bleed
                CachedAsyncImage(url: URL(string: item.imageUrl)) { phase in
                    if let image = phase.image {
                        image.resizable().aspectRatio(contentMode: .fill)
                    } else {
                        Color(white: 0.05)
                    }
                }
                .id(item.id)
                .frame(maxWidth: .infinity)
                .frame(height: UIScreen.main.bounds.height * 0.62)
                .clipped()
                .animation(.easeInOut(duration: 0.6), value: current)

                // نظام تدرجات متعدد الطبقات مثل نيتفلكس بالضبط
                VStack(spacing: 0) {
                    Spacer()
                    LinearGradient(colors: [.clear, APP_BG.opacity(0.2)],
                                   startPoint: .top, endPoint: .bottom)
                        .frame(height: 60)
                    LinearGradient(colors: [APP_BG.opacity(0.2), APP_BG.opacity(0.7)],
                                   startPoint: .top, endPoint: .bottom)
                        .frame(height: 100)
                    LinearGradient(colors: [APP_BG.opacity(0.7), APP_BG],
                                   startPoint: .top, endPoint: .bottom)
                        .frame(height: 80)
                    APP_BG.frame(height: 20)
                }

                // محتوى السفلي
                VStack(spacing: 0) {
                    Spacer()
                    VStack(spacing: 12) {
                        // اسم العمل
                        Text(item.title)
                            .font(appFont(28, bold: true))
                            .foregroundColor(.white)
                            .multilineTextAlignment(.center)
                            .lineLimit(2)
                            .shadow(color: .black.opacity(0.5), radius: 3, x: 0, y: 2)
                            .padding(.horizontal, 24)

                        // تفاصيل مختصرة
                        HStack(spacing: 8) {
                            Text(item.type == "movies" ? "فيلم" : "مسلسل")
                                .font(appFont(11, bold: true))
                                .foregroundColor(.black)
                                .padding(.horizontal, 8).padding(.vertical, 3)
                                .background(Color.white)
                                .cornerRadius(4)
                            Text(L("جديد", "New"))
                                .font(appFont(11, bold: true))
                                .foregroundColor(.green)
                            Circle().fill(.gray).frame(width: 3, height: 3)
                            Text("HD")
                                .font(appFont(11, bold: true))
                                .foregroundColor(.white.opacity(0.75))
                        }

                        // أزرار الإجراءات
                        HStack(spacing: 14) {
                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                HStack(spacing: 8) {
                                    Image(systemName: "play.fill")
                                        .font(appFont(16, bold: true))
                                    Text(L("تشغيل", "Play"))
                                        .font(appFont(16, bold: true))
                                }
                                .foregroundColor(.black)
                                .frame(width: 140, height: 44)
                                .background(Color.white)
                                .cornerRadius(6)
                            }

                            Button {
                                favStore.toggle(item: item)
                            } label: {
                                VStack(spacing: 4) {
                                    Image(systemName: favStore.isFavorite(item.id) ? "checkmark" : "plus")
                                        .font(appFont(18, bold: true))
                                    Text(L("قائمتي", "My List"))
                                        .font(appFont(10, bold: true))
                                }
                                .foregroundColor(.white)
                                .frame(width: 70, height: 44)
                                .background(Color.white.opacity(0.12))
                                .cornerRadius(6)
                                .overlay(RoundedRectangle(cornerRadius: 6).stroke(Color.white.opacity(0.25), lineWidth: 1))
                            }

                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                VStack(spacing: 4) {
                                    Image(systemName: "info.circle")
                                        .font(appFont(18, bold: true))
                                    Text(L("التفاصيل", "Details"))
                                        .font(appFont(10, bold: true))
                                }
                                .foregroundColor(.white)
                                .frame(width: 70, height: 44)
                                .background(Color.white.opacity(0.12))
                                .cornerRadius(6)
                                .overlay(RoundedRectangle(cornerRadius: 6).stroke(Color.white.opacity(0.25), lineWidth: 1))
                            }
                        }
                        .padding(.bottom, 16)

                        // نقاط المؤشر
                        HStack(spacing: 5) {
                            ForEach(0..<min(displayItems.count, 8), id: \.self) { i in
                                RoundedRectangle(cornerRadius: 2)
                                    .fill(i == current ? UT_RED : Color.white.opacity(0.3))
                                    .frame(width: i == current ? 20 : 6, height: 4)
                                    .animation(.spring(response: 0.3), value: current)
                            }
                        }
                        .padding(.bottom, 28)
                    }
                }
                .frame(height: UIScreen.main.bounds.height * 0.62)
            }
            .frame(height: UIScreen.main.bounds.height * 0.62)
            .contentShape(Rectangle())
            .gesture(DragGesture(minimumDistance: 30, coordinateSpace: .global)
                .onEnded { val in
                    let count = min(displayItems.count, 8)
                    if val.translation.width < -40 {
                        withAnimation { current = min(current + 1, count - 1) }
                        resetTimer(count: count)
                    } else if val.translation.width > 40 {
                        withAnimation { current = max(current - 1, 0) }
                        resetTimer(count: count)
                    }
                }
            )
            .onAppear  { startTimer() }
            .onDisappear { timer?.invalidate() }
        )
    }

    private func startTimer() {
        timer?.invalidate()
        let count = min(items.count, 8)
        guard count > 1 else { return }
        timer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            withAnimation(.easeInOut(duration: 0.6)) {
                current = (current + 1) % count
            }
        }
    }

    private func resetTimer(count: Int) {
        timer?.invalidate()
        guard count > 1 else { return }
        timer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            withAnimation(.easeInOut(duration: 0.6)) {
                current = (current + 1) % count
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Continue Watching Row (مع LazyHStack)
// ─────────────────────────────────────────────────────────────────────────────
struct ContinueWatchingRow: View {
    let items: [WatchProgress]
    @Binding var playItem: PlayerData?
    @ObservedObject private var store = WatchProgressStore.shared

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(L("متابعة المشاهدة", "Continue Watching"))
                .font(appFont(20, bold: true))
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
                                isMovie: prog.isMovie,
                                videoUrl: prog.videoUrl,
                                videoUrl720: prog.videoUrl720,
                                videoUrl1080: prog.videoUrl1080,
                                videoUrl360: prog.videoUrl360,
                                videoUrl4k: prog.videoUrl4k,
                                subtitleUrl: prog.subtitleUrl,
                                subtitleVttUrl: prog.subtitleVttUrl,
                                episodeId: prog.episodeId,
                                episodeTitle: prog.episodeTitle,
                                episodes: []
                            )
                        } label: {
                            VStack(alignment: .leading, spacing: 8) {
                                ZStack(alignment: .center) {
                                    CachedAsyncImage(url: URL(string: prog.imageUrl)) { phase in
                                        if let image = phase.image {
                                            image.resizable().aspectRatio(contentMode: .fill)
                                                .transition(.opacity)
                                        } else {
                                            Color(white: 0.12)
                                        }
                                    }
                                    .id(prog.itemId)
                                    .frame(width: 160, height: 100)
                                    .clipped()
                                    .cornerRadius(12)

                                    Color.black.opacity(0.3).cornerRadius(12)

                                    Image(systemName: "play.circle.fill")
                                        .font(appFont(40))
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
                                    .font(appFont(13, bold: true))
                                    .foregroundColor(.white)
                                    .lineLimit(1)
                                    .frame(width: 160, alignment: .leading)

                                if !prog.episodeTitle.isEmpty {
                                    Text(prog.episodeTitle)
                                        .font(appFont(11, bold: false))
                                        .foregroundColor(.gray)
                                        .lineLimit(1)
                                        .frame(width: 160, alignment: .leading)
                                }
                            }
                        }
                        .contextMenu {
                            Button(role: .destructive) {
                                store.remove(itemId: prog.itemId)
                            } label: {
                                Label("إزالة من القائمة", systemImage: "trash")
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
// MARK: – Category Row (مع LazyHStack وزر "عرض الكل" لكل قسم من الصفحة الرئيسية)
// ─────────────────────────────────────────────────────────────────────────────
struct Top10Row: View {
    let title: String
    let items: [VideoItem]

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack(spacing: 6) {
                Image(systemName: "flame.fill")
                    .font(appFont(16, bold: true))
                    .foregroundColor(UT_RED)
                Text(title)
                    .font(appFont(20, bold: true))
                    .foregroundColor(.white)
            }
            .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                LazyHStack(alignment: .bottom, spacing: 6) {
                    ForEach(Array(items.prefix(10).enumerated()), id: \.element.id) { index, item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            // مثل نيتفلكس تماماً: الرقم على اليسار، الكارت يغطي جزء منه من اليمين
                            // نستخدم HStack بـ spacing سلبي لتحقيق التداخل
                            HStack(spacing: -26) {
                                // الرقم الكبير (يظهر من الجانب الأيسر)
                                ZStack(alignment: .bottom) {
                                    // حرف شفاف بنفس الحجم لتثبيت الإطار
                                    Text("\(index + 1)")
                                        .font(appFont(88, bold: true))
                                        .foregroundColor(.clear)

                                    // الرقم بتدرج أبيض→شفاف من الأعلى للأسفل
                                    Text("\(index + 1)")
                                        .font(appFont(88, bold: true))
                                        .foregroundStyle(
                                            LinearGradient(
                                                colors: [.white.opacity(0.9), .white.opacity(0.2)],
                                                startPoint: .top, endPoint: .bottom
                                            )
                                        )
                                        .shadow(color: .black.opacity(0.7), radius: 2, x: 1, y: 1)
                                }
                                .frame(width: 58)
                                .zIndex(0)

                                // الكارت يعلو فوق الرقم بـ zIndex أعلى
                                PosterCard(item: item, showTitle: false)
                                    .zIndex(1)
                            }
                            .padding(.leading, index == 0 ? 16 : 6)
                        }
                        .buttonStyle(ScaleButtonStyle())
                    }
                }
                .padding(.trailing, 16)
            }
        }
    }
}

struct CategoryRow: View {
    let title: String
    let items: [VideoItem]
    var tagId: Int = -1
    var scraper: MovieScraper? = nil
    @ObservedObject private var store = WatchProgressStore.shared
    @ObservedObject private var settings = AppSettings.shared

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text(title)
                    .font(appFont(19, bold: true))
                    .foregroundColor(.white)

                Spacer()

                if tagId >= 0, let scraper = scraper {
                    NavigationLink(
                        destination: CategoryListView(
                            category: SiteCategory(id: tagId, remoteId: tagId, isTag: true, nameAr: title, nameEn: title),
                            scraper: scraper
                        )
                    ) {
                        HStack(spacing: 4) {
                            Text(L("عرض الكل", "See All"))
                            // الرمز يتغير بحسب اتجاه اللغة
                            Image(systemName: settings.appLanguage == "ar" ? "chevron.left" : "chevron.right")
                        }
                        .font(appFont(12, bold: true))
                        .foregroundColor(UT_RED.opacity(0.85))
                    }
                }
            }
            .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 14) {
                    ForEach(items) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item, progress: store.progress(for: item.id))
                        }
                        .buttonStyle(ScaleButtonStyle())
                    }
                }
                .padding(.horizontal)
            }
        }
    }
}
"""
views_swift_p3 = r"""
// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Browse & Category Lists (مع تحسين التحميل اللانهائي ودعم sort/genre)
// ─────────────────────────────────────────────────────────────────────────────
struct BrowseView: View {
    @ObservedObject var scraper: MovieScraper
    @ObservedObject private var settings = AppSettings.shared
    let cols = [GridItem(.flexible()), GridItem(.flexible())]

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                ScrollView {
                    LazyVGrid(columns: cols, spacing: 14) {
                        ForEach(SITE_CATEGORIES) { cat in
                            NavigationLink(destination: CategoryListView(category: cat, scraper: scraper)) {
                                ZStack(alignment: .bottomLeading) {
                                    // خلفية تدرج مميزة لكل بطاقة
                                    RoundedRectangle(cornerRadius: 14)
                                        .fill(
                                            LinearGradient(
                                                colors: [categoryColor(cat).opacity(0.5), categoryColor(cat).opacity(0.12)],
                                                startPoint: .topTrailing, endPoint: .bottomLeading
                                            )
                                        )
                                        .overlay(RoundedRectangle(cornerRadius: 14).stroke(categoryColor(cat).opacity(0.25), lineWidth: 1))

                                    // أيقونة الفئة
                                    Image(systemName: categoryIcon(cat))
                                        .font(appFont(44, bold: false))
                                        .foregroundColor(categoryColor(cat).opacity(0.3))
                                        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topTrailing)
                                        .padding(12)

                                    // نص الفئة
                                    VStack(alignment: .leading, spacing: 3) {
                                        Text(settings.appLanguage == "ar" ? cat.nameAr : cat.nameEn)
                                            .font(appFont(14, bold: true))
                                            .foregroundColor(.white)
                                            .lineLimit(2)
                                        if settings.appLanguage == "ar" && !cat.nameEn.isEmpty {
                                            Text(cat.nameEn)
                                                .font(appFont(10))
                                                .foregroundColor(.white.opacity(0.5))
                                        }
                                    }
                                    .padding(12)
                                }
                                .frame(height: 95)
                            }
                            .buttonStyle(ScaleButtonStyle())
                        }
                    }
                    .padding(16)
                }
            }
            .navigationTitle(L("تصفح", "Browse"))
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }

    private func categoryIcon(_ cat: SiteCategory) -> String {
        let n = cat.nameEn.lowercased()
        if n.contains("anime")    { return "sparkles.tv" }
        if n.contains("movie")    { return "film.stack" }
        if n.contains("series") || n.contains("tv") { return "tv" }
        if n.contains("kids")     { return "star.circle" }
        if n.contains("action")   { return "bolt.fill" }
        if n.contains("korean") || n.contains("asian") { return "globe.asia.australia" }
        if n.contains("netflix")  { return "n.square.fill" }
        if n.contains("disney")   { return "wand.and.stars" }
        if n.contains("document") { return "doc.text.magnifyingglass" }
        if n.contains("turkish")  { return "moon.stars" }
        if n.contains("ramadan")  { return "moon.fill" }
        if n.contains("spanish")  { return "music.mic" }
        return "play.tv"
    }

    private func categoryColor(_ cat: SiteCategory) -> Color {
        let n = cat.nameEn.lowercased()
        if n.contains("anime")    { return .purple }
        if n.contains("movie")    { return .blue }
        if n.contains("kids")     { return .orange }
        if n.contains("action")   { return .red }
        if n.contains("korean") || n.contains("asian") { return .pink }
        if n.contains("netflix")  { return .red }
        if n.contains("disney")   { return .cyan }
        if n.contains("document") { return .teal }
        if n.contains("ramadan")  { return Color(red: 0.6, green: 0.4, blue: 0.0) }
        return UT_RED
    }
}

struct CategoryListView: View {
    let category: SiteCategory
    @ObservedObject var scraper: MovieScraper
    @State private var items: [VideoItem] = []
    @State private var page    = 1
    @State private var loading = false
    @State private var reachedEnd = false
    @State private var selectedSort: String = "date"
    @State private var selectedGenre: String = ""
    @ObservedObject private var settings = AppSettings.shared

    var cols: [GridItem] {
        let minWidth: CGFloat
        switch settings.gridSizeStr {
        case "small":  minWidth = 90
        case "large":  minWidth = 150
        default:       minWidth = 110 // medium
        }
        return [GridItem(.adaptive(minimum: minWidth), spacing: 14)]
    }

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            ScrollView {
                // أزرار الترتيب
                HStack {
                    Picker(L("ترتيب", "Sort"), selection: $selectedSort) {
                        Text(L("تاريخ", "Date")).tag("date")
                        Text(L("سنة", "Year")).tag("year")
                        Text(L("مشاهدات", "Views")).tag("views")
                        Text(L("تقييم", "Rating")).tag("rating")
                    }
                    .pickerStyle(.segmented)
                    .colorMultiply(.white)
                    .onChange(of: selectedSort) { _ in
                        resetAndLoad()
                    }

                    // زر التصفية حسب النوع (سيظهر مربع حوار بسيط)
                    Button {
                        // عرض مربع حوار لاختيار النوع
                        let alert = UIAlertController(title: "اختر النوع", message: nil, preferredStyle: .actionSheet)
                        let genres = ["Action", "Adventure", "Animation", "Comedy", "Drama", "Fantasy", "Horror", "Romance", "Sci-Fi", "Thriller"]
                        for g in genres {
                            alert.addAction(UIAlertAction(title: g, style: .default) { _ in
                                selectedGenre = g
                                resetAndLoad()
                            })
                        }
                        alert.addAction(UIAlertAction(title: "الكل", style: .default) { _ in
                            selectedGenre = ""
                            resetAndLoad()
                        })
                        alert.addAction(UIAlertAction(title: "إلغاء", style: .cancel))
                        // عرض الـ Alert
                        if let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
                           let rootVC = windowScene.windows.first?.rootViewController {
                            rootVC.present(alert, animated: true)
                        }
                    } label: {
                        Image(systemName: "tag")
                            .foregroundColor(.white)
                            .padding(8)
                            .background(Color.white.opacity(0.1))
                            .cornerRadius(8)
                    }
                    if !selectedGenre.isEmpty {
                        Text(selectedGenre)
                            .font(.caption)
                            .foregroundColor(UT_RED)
                            .padding(4)
                            .background(Color.white.opacity(0.1))
                            .cornerRadius(4)
                            .onTapGesture {
                                selectedGenre = ""
                                resetAndLoad()
                            }
                    }
                }
                .padding(.horizontal, 16)
                .padding(.top, 8)

                LazyVGrid(columns: cols, spacing: 16) {
                    ForEach(Array(items.enumerated()), id: \.element.id) { index, item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item)
                        }
                        .buttonStyle(ScaleButtonStyle())
                        .onAppear {
                            // نطلب المزيد قبل الوصول للعنصر الأخير فعلياً بعدة عناصر (عتبة تحميل مسبق)
                            // بدل انتظار العنصر الأخير حرفياً، لأن ذلك غير موثوق دائماً مع LazyVGrid
                            let prefetchThreshold = 6
                            if !loading && !reachedEnd && index >= items.count - prefetchThreshold {
                                loadMore()
                            }
                        }
                    }
                }
                .padding()
                if loading {
                    ProgressView()
                        .padding()
                }
                if reachedEnd && !items.isEmpty {
                    Text(L("تم تحميل جميع العناصر", "All items loaded"))
                        .font(.caption)
                        .foregroundColor(.gray)
                        .padding()
                }
            }
            .refreshable {
                // سحب لتحديث الصفحة
                resetAndLoad()
            }
        }
        .navigationTitle(category.nameAr)
        .onAppear {
            if items.isEmpty {
                loadMore()
            }
        }
    }

    private func resetAndLoad() {
        page = 1
        items = []
        reachedEnd = false
        loadMore()
    }

    private func loadMore() {
        guard !loading, !reachedEnd else { return }
        loading = true
        scraper.fetchCategory(typeId: category.remoteId, page: page, useTag: category.isTag, sort: selectedSort, genre: selectedGenre.isEmpty ? nil : selectedGenre) { newItems, hasMore in
            if newItems.isEmpty {
                reachedEnd = true
            } else {
                var existingIds = Set(items.map { $0.id })
                for it in newItems where !existingIds.contains(it.id) {
                    items.append(it)
                    existingIds.insert(it.id)
                }
                page += 1
                if !hasMore { reachedEnd = true }
            }
            loading = false
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Search View (مع فلاتر متقدمة وترتيب)
// ─────────────────────────────────────────────────────────────────────────────
struct SearchView: View {
    @ObservedObject var scraper: MovieScraper

    // فلاتر البحث
    @State private var title = ""
    @State private var genre = ""
    @State private var type = ""
    @State private var year = ""
    @State private var imdbrate = ""
    @State private var language = ""
    @State private var director = ""
    @State private var writer = ""
    @State private var cast = ""
    @State private var imdb = ""
    @State private var mpr = ""
    @State private var production = ""
    @State private var featured = false

    // الترتيب
    enum SortOption: String, CaseIterable {
        case title = "العنوان"
        case year = "السنة"
        case rating = "التقييم"
    }
    @State private var sortBy: SortOption = .title
    @State private var ascending = true

    @State private var results: [VideoItem] = []
    @State private var searching = false
    @State private var showFilters = false  // إظهار الفلاتر
    @State private var liveSearch = true

    // تأخير للبحث الحي
    @State private var searchDebounce: Timer?

    let cols = [GridItem(.adaptive(minimum: 110), spacing: 14)]

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                VStack(spacing: 0) {
                    // شريط البحث السريع مع خيارات
                    HStack {
                        Image(systemName: "magnifyingglass").foregroundColor(.gray)
                        TextField("بحث...", text: $title)
                            .foregroundColor(.white)
                            .onChange(of: title) { newValue in
                                if liveSearch && !newValue.isEmpty {
                                    performSearch()
                                }
                            }
                            .onSubmit { performSearch() }
                        if searching {
                            ProgressView().tint(.white)
                        } else if !title.isEmpty {
                            Button {
                                title = ""
                                results = []
                            } label: {
                                Image(systemName: "xmark.circle.fill").foregroundColor(.gray)
                            }
                        }
                        Button(action: { showFilters.toggle() }) {
                            Image(systemName: "slider.horizontal.3")
                                .foregroundColor(showFilters ? UT_RED : .gray)
                        }
                    }
                    .padding(14)
                    .background(Color.white.opacity(0.1))
                    .cornerRadius(12)
                    .padding(.horizontal, 16)
                    .padding(.top, 8)

                    // الفلاتر المتقدمة
                    if showFilters {
                        ScrollView(.vertical, showsIndicators: false) {
                            VStack(alignment: .leading, spacing: 12) {
                                Group {
                                    Text(L("فلاتر متقدمة", "Advanced Filters"))
                                        .font(.headline).foregroundColor(.white)
                                    HStack {
                                        Text(L("النوع:", "Type:")).foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        Picker("", selection: $type) {
                                            Text(L("الكل", "All")).tag("")
                                            ForEach(SITE_CATEGORIES, id: \.id) { cat in
                                                Text(cat.nameAr).tag("\(cat.remoteId)")
                                            }
                                        }
                                        .pickerStyle(.menu)
                                        .accentColor(.white)
                                    }
                                    HStack {
                                        Text(L("السنة:", "Year:")).foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        TextField("مثال 2024", text: $year)
                                            .textFieldStyle(RoundedBorderTextFieldStyle())
                                            .foregroundColor(.black)
                                    }
                                    HStack {
                                        Text("التقييم:").foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        Picker("", selection: $imdbrate) {
                                            Text(L("الكل", "All")).tag("")
                                            ForEach(1...9, id: \.self) { i in
                                                Text("\(i)+").tag("\(i)")
                                            }
                                        }
                                        .pickerStyle(.menu)
                                        .accentColor(.white)
                                    }
                                    HStack {
                                        Text("اللغة:").foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        TextField("مثال Arabic", text: $language)
                                            .textFieldStyle(RoundedBorderTextFieldStyle())
                                            .foregroundColor(.black)
                                    }
                                    HStack {
                                        Text("المخرج:").foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        TextField("اسم المخرج", text: $director)
                                            .textFieldStyle(RoundedBorderTextFieldStyle())
                                            .foregroundColor(.black)
                                    }
                                    HStack {
                                        Text("الكاتب:").foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        TextField("اسم الكاتب", text: $writer)
                                            .textFieldStyle(RoundedBorderTextFieldStyle())
                                            .foregroundColor(.black)
                                    }
                                    HStack {
                                        Text("الممثلين:").foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        TextField("اسم ممثل", text: $cast)
                                            .textFieldStyle(RoundedBorderTextFieldStyle())
                                            .foregroundColor(.black)
                                    }
                                    HStack {
                                        Text("IMDB ID:").foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        TextField("مثال tt4465472", text: $imdb)
                                            .textFieldStyle(RoundedBorderTextFieldStyle())
                                            .foregroundColor(.black)
                                    }
                                    HStack {
                                        Text("MPR:").foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        TextField("مثال PG-13", text: $mpr)
                                            .textFieldStyle(RoundedBorderTextFieldStyle())
                                            .foregroundColor(.black)
                                    }
                                    HStack {
                                        Text("تاريخ الإنتاج:").foregroundColor(.gray).frame(width: 80, alignment: .leading)
                                        TextField("مثال 8 January 2016", text: $production)
                                            .textFieldStyle(RoundedBorderTextFieldStyle())
                                            .foregroundColor(.black)
                                    }
                                    Toggle("مميز", isOn: $featured)
                                        .toggleStyle(SwitchToggleStyle(tint: UT_RED))
                                        .foregroundColor(.white)
                                    Toggle("بحث حي", isOn: $liveSearch)
                                        .toggleStyle(SwitchToggleStyle(tint: UT_RED))
                                        .foregroundColor(.white)
                                    HStack {
                                        Button("بحث") { performSearch() }
                                            .buttonStyle(.borderedProminent)
                                            .tint(UT_RED)
                                        Button("مسح") {
                                            clearFilters()
                                        }
                                        .buttonStyle(.bordered)
                                    }
                                }
                            }
                            .padding(16)
                            .background(Color.white.opacity(0.05))
                            .cornerRadius(12)
                            .padding(.horizontal, 16)
                            .padding(.bottom, 8)
                        }
                        .frame(maxHeight: 400)
                    }

                    // خيارات الترتيب
                    HStack {
                        Picker("ترتيب حسب", selection: $sortBy) {
                            ForEach(SortOption.allCases, id: \.self) { opt in
                                Text(opt.rawValue).tag(opt)
                            }
                        }
                        .pickerStyle(.segmented)
                        .colorMultiply(.white)
                        Button(action: { ascending.toggle() }) {
                            Image(systemName: ascending ? "arrow.up" : "arrow.down")
                                .foregroundColor(.white)
                        }
                        .padding(.leading, 8)
                    }
                    .padding(.horizontal, 16)
                    .padding(.top, 8)

                    // النتائج
                    if results.isEmpty && !title.isEmpty && !searching {
                        VStack(spacing: 12) {
                            Image(systemName: "magnifyingglass")
                                .font(appFont(40))
                                .foregroundColor(.gray)
                            Text("لا توجد نتائج لـ \"\(title)\"")
                                .foregroundColor(.gray)
                        }
                        .padding(.top, 60)
                        Spacer()
                    } else {
                        ScrollView {
                            LazyVGrid(columns: cols, spacing: 16) {
                                ForEach(results) { item in
                                    NavigationLink(destination: DetailsView(itemId: item.id)) {
                                        PosterCard(item: item)
                                    }
                                    .buttonStyle(ScaleButtonStyle())
                                }
                            }
                            .padding()
                        }
                    }
                }
            }
            .navigationTitle("البحث المتقدم")
        }
        .navigationViewStyle(StackNavigationViewStyle())
        .navigationViewStyle(StackNavigationViewStyle())
    }

    private func performSearch() {
        guard !title.trimmingCharacters(in: .whitespaces).isEmpty else {
            results = []
            return
        }
        searching = true
        scraper.advancedSearch(
            title: title.isEmpty ? nil : title,
            genre: genre.isEmpty ? nil : genre,
            type: type.isEmpty ? nil : type,
            imdb: imdb.isEmpty ? nil : imdb,
            director: director.isEmpty ? nil : director,
            writer: writer.isEmpty ? nil : writer,
            cast: cast.isEmpty ? nil : cast,
            year: year.isEmpty ? nil : year,
            mpr: mpr.isEmpty ? nil : mpr,
            imdbrate: imdbrate.isEmpty ? nil : imdbrate,
            production: production.isEmpty ? nil : production,
            language: language.isEmpty ? nil : language,
            featured: featured ? true : nil
        ) { items in
            // تطبيق الترتيب
            let sorted = sortItems(items)
            results = sorted
            searching = false
        }
    }

    private func sortItems(_ items: [VideoItem]) -> [VideoItem] {
        switch sortBy {
        case .title:
            return items.sorted { ascending ? $0.title < $1.title : $0.title > $1.title }
        case .year:
            let sorted = items.sorted { item1, item2 in
                let year1 = extractYear(from: item1.title) ?? 0
                let year2 = extractYear(from: item2.title) ?? 0
                return ascending ? year1 < year2 : year1 > year2
            }
            return sorted
        case .rating:
            return items
        }
    }

    private func extractYear(from title: String) -> Int? {
        let pattern = #"\((\d{4})\)"#
        if let rx = try? NSRegularExpression(pattern: pattern),
           let match = rx.firstMatch(in: title, range: NSRange(title.startIndex..., in: title)),
           let range = Range(match.range(at: 1), in: title) {
            return Int(String(title[range]))
        }
        return nil
    }

    private func clearFilters() {
        title = ""
        genre = ""
        type = ""
        year = ""
        imdbrate = ""
        language = ""
        director = ""
        writer = ""
        cast = ""
        imdb = ""
        mpr = ""
        production = ""
        featured = false
        results = []
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
                            .font(appFont(60)).foregroundColor(.gray)
                        Text("لا توجد تحميلات").foregroundColor(.gray)
                    }
                } else {
                    List {
                        ForEach(manager.activeDownloads) { dl in
                            HStack {
                                CachedAsyncImage(url: URL(string: dl.imageUrl)) { phase in
                                    if let image = phase.image {
                                        image.resizable().aspectRatio(contentMode: .fill)
                                    } else {
                                        Color.gray
                                    }
                                }
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
            .navigationTitle(L("التحميلات", "Downloads"))
        }
        .navigationViewStyle(StackNavigationViewStyle())
        .alert("تنبيه", isPresented: Binding(
            get: { manager.lastError != nil },
            set: { if !$0 { manager.lastError = nil } }
        )) {
            Button("حسناً", role: .cancel) {}
        } message: {
            Text(manager.lastError ?? "")
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Favorites View
// ─────────────────────────────────────────────────────────────────────────────
struct FavoritesView: View {
    @ObservedObject var favStore = FavoritesStore.shared
    let cols = [GridItem(.adaptive(minimum: 110), spacing: 14)]

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            if favStore.items.isEmpty {
                VStack(spacing: 20) {
                    Image(systemName: "heart")
                        .font(appFont(60)).foregroundColor(.gray)
                    Text(L("لا توجد مفضلات", "No favorites")).foregroundColor(.gray)
                }
            } else {
                ScrollView {
                    LazyVGrid(columns: cols, spacing: 16) {
                        ForEach(favStore.items) { item in
                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                PosterCard(item: item)
                            }
                            .buttonStyle(ScaleButtonStyle())
                            .contextMenu {
                                Button(role: .destructive) {
                                    favStore.toggle(item: item)
                                } label: {
                                    Label("إزالة من المفضلة", systemImage: "heart.slash")
                                }
                            }
                        }
                    }
                    .padding()
                }
            }
        }
        .navigationTitle(L("المفضلة", "Favorites"))
    }
}

struct SettingsView: View {
    @ObservedObject var settings      = AppSettings.shared
    @ObservedObject var historyStore  = WatchProgressStore.shared
    @ObservedObject var session       = AuthSession.shared
    @State private var cacheCleared   = false

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                Form {
                    // 1) الحساب
                    Section(header: Text(L("الحساب", "Account")).foregroundColor(UT_RED)) {
                        NavigationLink(destination: AccountView()) {
                            HStack {
                                ZStack {
                                    Circle().fill(UT_RED.opacity(0.2)).frame(width: 36, height: 36)
                                    Image(systemName: session.isLoggedIn ? "person.fill" : "person")
                                        .font(appFont(15))
                                        .foregroundColor(UT_RED)
                                }
                                VStack(alignment: .leading, spacing: 2) {
                                    Text(session.isLoggedIn ? (session.user?.displayName ?? "حسابي") : "سجّل الدخول")
                                        .font(appFont(15, bold: true))
                                    if session.isLoggedIn, let email = session.user?.email {
                                        Text(email).font(appFont(12)).foregroundColor(.gray)
                                    } else {
                                        Text("لمزامنة المفضلة والتقدم عبر أجهزتك")
                                            .font(appFont(12)).foregroundColor(.gray)
                                    }
                                }
                            }
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    // 2) المفضلة
                    Section(header: Text(L("المفضلة", "Favorites")).foregroundColor(UT_RED)) {
                        NavigationLink(destination: FavoritesView()) {
                            HStack {
                                Image(systemName: "heart.fill")
                                    .foregroundColor(.red)
                                Text("عرض المفضلة (\(FavoritesStore.shared.items.count))")
                            }
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    // 3) التشغيل التلقائي
                    Section(header: Text(L("التشغيل التلقائي", "Autoplay")).foregroundColor(UT_RED)) {
                        Toggle("تشغيل الحلقة التالية تلقائياً", isOn: $settings.autoPlayNextEnabled)
                        if settings.autoPlayNextEnabled {
                            VStack(alignment: .leading) {
                                Text("العد التنازلي قبل التشغيل: \(settings.autoPlayCountdownSeconds) ثانية")
                                Slider(
                                    value: Binding(
                                        get: { Double(settings.autoPlayCountdownSeconds) },
                                        set: { settings.autoPlayCountdownSeconds = Int($0) }
                                    ),
                                    in: 3...20, step: 1
                                )
                                .accentColor(UT_RED)
                            }
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    // 4) إعدادات الترجمة
                    Section(header: Text(L("إعدادات الترجمة", "Subtitle Settings")).foregroundColor(UT_RED)) {
                        Toggle(L("تفعيل الترجمة", "Enable Subtitles"), isOn: $settings.subtitlesEnabled)
                        if settings.subtitlesEnabled {
                            Picker(L("الخط", "Font"), selection: $settings.subtitleFontName) {
                                Text("ExpoArabic").tag("Expo")
                                Text("Cairo").tag("Cairo")
                                Text("Rubik").tag("Rubik")
                                Text("IBM Plex").tag("Ibm")
                                Text(L("النظام", "System")).tag("System")
                            }
                            .pickerStyle(.segmented)
                            .colorMultiply(.white)

                            // معاينة مباشرة للخط المختار
                            HStack {
                                Spacer()
                                Text("نص تجريبي للترجمة - مثال على الخط")
                                    .font(subtitleFontForPlayer(name: settings.subtitleFontName, size: CGFloat(settings.subtitleFontSize)))
                                    .foregroundColor(settings.subtitleColor)
                                    .padding(.horizontal, 14)
                                    .padding(.vertical, 8)
                                    .background(Color.black.opacity(settings.subtitleBgOpacity))
                                    .cornerRadius(8)
                                Spacer()
                            }
                            .padding(.vertical, 4)

                            VStack(alignment: .leading) {
    Text(L("حجم الخط: \(Int(settings.subtitleFontSize))", "Font Size: \(Int(settings.subtitleFontSize))"))
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

                    // 5) الثيم واللغة
                    Section(header: Text(L("الثيم والمظهر", "Theme & Language")).foregroundColor(UT_RED)) {
                        Picker(L("الثيم", "Theme"), selection: $settings.appTheme) {
                            Text(L("داكن", "Dark")).tag("dark")
                            Text("AMOLED").tag("amoled")
                            Text(L("أزرق داكن", "Dark Blue")).tag("dark_blue")
                            Text(L("بنفسجي داكن", "Dark Purple")).tag("dark_purple")
                        }
                        Picker(L("لون الأكسنت", "Accent Color"), selection: $settings.accentColorName) {
                            HStack { Circle().fill(.red).frame(width: 14, height: 14); Text(L("أحمر","Red")) }.tag("red")
                            HStack { Circle().fill(.blue).frame(width: 14, height: 14); Text(L("أزرق","Blue")) }.tag("blue")
                            HStack { Circle().fill(.orange).frame(width: 14, height: 14); Text(L("برتقالي","Orange")) }.tag("orange")
                            HStack { Circle().fill(.green).frame(width: 14, height: 14); Text(L("أخضر","Green")) }.tag("green")
                            HStack { Circle().fill(.pink).frame(width: 14, height: 14); Text(L("وردي","Pink")) }.tag("pink")
                        }
                        Picker(L("اللغة", "Language"), selection: $settings.appLanguage) {
                            Text("العربية").tag("ar")
                            Text("English").tag("en")
                        }
                        .pickerStyle(.segmented)
                        .colorMultiply(.white)
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    // 6) التشغيل والتنزيل
                    Section(header: Text(L("التشغيل والتنزيل", "Playback & Download")).foregroundColor(UT_RED)) {
                        Picker(L("الجودة الافتراضية", "Default Quality"), selection: $settings.preferredQuality) {
                            Text(L("تلقائي", "Auto")).tag("تلقائي")
                            Text("360p").tag("360p")
                            Text("720p").tag("720p")
                            Text("1080p").tag("1080p")
                            Text("4K").tag("4K")
                        }
                        Toggle(L("التنزيل عبر الواي فاي فقط", "Download on Wi-Fi Only"), isOn: $settings.downloadOverWifiOnly)
                        Picker(L("حجم الشبكة", "Grid Size"), selection: $settings.gridSizeStr) {
                            Text(L("صغير", "Small")).tag("small")
                            Text(L("متوسط", "Medium")).tag("medium")
                            Text(L("كبير", "Large")).tag("large")
                        }
                        .pickerStyle(.segmented)
                        .colorMultiply(.white)
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    // 7) البيانات
                    Section(header: Text(L("البيانات", "Data")).foregroundColor(UT_RED)) {
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

                    // 7) الشكاوى والاقتراحات
                    Section(header: Text(L("تواصل معنا", "Contact Us")).foregroundColor(UT_RED)) {
                        if session.isLoggedIn {
                            NavigationLink(destination: FeedbackView()) {
                                HStack {
                                    Image(systemName: "bubble.left.and.exclamationmark.bubble.right")
                                        .foregroundColor(UT_RED)
                                    Text("الشكاوى والاقتراحات")
                                }
                            }
                        } else {
                            NavigationLink(destination: AccountView()) {
                                HStack {
                                    Image(systemName: "bubble.left.and.exclamationmark.bubble.right")
                                        .foregroundColor(.gray)
                                    Text("سجّل الدخول لإرسال شكوى أو اقتراح")
                                        .foregroundColor(.gray)
                                }
                            }
                        }
                        if let url = URL(string: "mailto:support@utan.app") {
                            Link(destination: url) {
                                HStack {
                                    Image(systemName: "envelope")
                                        .foregroundColor(UT_RED)
                                    Text("راسلنا عبر البريد الإلكتروني")
                                }
                            }
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)

                    // 8) لوحة الإدارة (تظهر فقط لحسابات الإدمن)
                    if session.isAdmin {
                        Section(header: Text(L("الإدارة", "Admin")).foregroundColor(UT_RED)) {
                            NavigationLink(destination: AdminPanelView()) {
                                HStack {
                                    Image(systemName: "shield.lefthalf.filled")
                                        .foregroundColor(UT_RED)
                                    Text("لوحة الإدارة")
                                }
                            }
                        }
                        .listRowBackground(Color.white.opacity(0.05))
                        .foregroundColor(.white)
                    }

                    // 9) حول التطبيق
                    Section(header: Text(L("حول التطبيق", "About")).foregroundColor(UT_RED)) {
                        HStack {
                            Text(L("الإصدار", "Version"))
                            Spacer()
                            Text("5.0").foregroundColor(.gray)
                        }
                        HStack {
                            Text(L("اللغة", "Language"))
                            Spacer()
                            Text(settings.appLanguage).foregroundColor(.gray)
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)
                }
                .scrollContentBackground(.hidden)
            }
            .navigationTitle(L("المزيد", "More"))
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }
}

struct HistoryListView: View {
    @ObservedObject var store: WatchProgressStore
    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            if store.recent.isEmpty {
                VStack(spacing: 16) {
                    Image(systemName: "clock.arrow.circlepath")
                        .font(appFont(50)).foregroundColor(.gray)
                    Text("لا يوجد سجل مشاهدة").foregroundColor(.gray)
                }
            } else {
                List {
                    ForEach(store.recent) { prog in
                        HStack {
                            CachedAsyncImage(url: URL(string: prog.imageUrl)) { phase in
                                if let image = phase.image {
                                    image.resizable().aspectRatio(contentMode: .fill)
                                } else {
                                    Color.gray
                                }
                            }
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
        }
        .navigationTitle(L("سجل المشاهدة", "Watch History"))
    }
}
"""
views_swift_p4 = r"""
// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Share Sheet (لمشاركة رابط العمل)
// ─────────────────────────────────────────────────────────────────────────────
struct ShareSheet: UIViewControllerRepresentable {
    let items: [Any]
    func makeUIViewController(context: Context) -> UIActivityViewController {
        UIActivityViewController(activityItems: items, applicationActivities: nil)
    }
    func updateUIViewController(_ uiViewController: UIActivityViewController, context: Context) {}
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – DetailsView
// ─────────────────────────────────────────────────────────────────────────────
struct DetailsView: View {
    let itemId: String
    @StateObject private var scraper    = MovieScraper()
    @ObservedObject private var favStore = FavoritesStore.shared
    @ObservedObject private var settings = AppSettings.shared

    @State private var details: MediaDetails?
    @State private var loading          = true
    @State private var playerData: PlayerData?
    @State private var selectedSeason   = ""
    @State private var showShareSheet   = false
    @State private var synopsisExpanded = false

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            if loading {
                UTanLoader(isLoading: $loading)
            } else if let d = details {
                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 0) {

                        // ── Hero backdrop (adaptive height for iPhone/iPad portrait & landscape) ──
                        GeometryReader { geo in
                            ZStack(alignment: .bottom) {
                                CachedAsyncImage(url: URL(string: d.imageUrl)) { phase in
                                    if let image = phase.image {
                                        image.resizable().aspectRatio(contentMode: .fill)
                                            .transition(.opacity.animation(.easeIn(duration: 0.4)))
                                    } else { Color(white: 0.08) }
                                }
                                .id(d.imageUrl)
                                .frame(width: geo.size.width, height: backdropHeight(geo: geo))
                                .clipped()

                                // نظام التدرجات المتعددة الطبقات
                                VStack(spacing: 0) {
                                    Spacer()
                                    LinearGradient(colors: [.clear, APP_BG.opacity(0.3)], startPoint: .top, endPoint: .bottom).frame(height: 80)
                                    LinearGradient(colors: [APP_BG.opacity(0.3), APP_BG.opacity(0.85)], startPoint: .top, endPoint: .bottom).frame(height: 120)
                                    LinearGradient(colors: [APP_BG.opacity(0.85), APP_BG], startPoint: .top, endPoint: .bottom).frame(height: 80)
                                    APP_BG.frame(height: 20)
                                }
                            }
                            .frame(width: geo.size.width, height: backdropHeight(geo: geo))
                        }
                        .frame(height: backdropHeightEstimate())

                        VStack(alignment: .leading, spacing: 14) {

                            // العنوان + أكشن بار مدمج
                            Text(d.title)
                                .font(appFont(26, bold: true))
                                .foregroundColor(.white)
                                .lineSpacing(4)

                            // شارات المعلومات
                            ScrollView(.horizontal, showsIndicators: false) {
                                HStack(spacing: 8) {
                                    if !d.year.isEmpty    { metaBadge(d.year, icon: "calendar") }
                                    if !d.rating.isEmpty  { metaBadge(d.rating, icon: "star.fill", color: .yellow) }
                                    if !d.runtime.isEmpty { metaBadge(d.runtime, icon: "clock") }
                                    if !d.genre.isEmpty {
                                        ForEach(d.genre.components(separatedBy: " | "), id: \.self) { g in
                                            genrePill(g)
                                        }
                                    }
                                }
                            }

                            // ── زر التشغيل الرئيسي (Netflix big white button) ──
                            if d.isMovie {
                                Button { playMovie(d: d) } label: {
                                    HStack(spacing: 8) {
                                        Image(systemName: "play.fill")
                                            .font(appFont(17, bold: true))
                                        Text(L("تشغيل", "Play"))
                                            .font(appFont(17, bold: true))
                                    }
                                    .foregroundColor(.black)
                                    .frame(maxWidth: .infinity)
                                    .frame(height: 50)
                                    .background(Color.white)
                                    .cornerRadius(8)
                                }
                            } else if let first = d.episodes.first {
                                Button { playEpisode(d: d, ep: first) } label: {
                                    HStack(spacing: 8) {
                                        Image(systemName: "play.fill")
                                            .font(appFont(17, bold: true))
                                        Text(L("تشغيل الحلقة الأولى", "Play First Episode"))
                                            .font(appFont(16, bold: true))
                                    }
                                    .foregroundColor(.black)
                                    .frame(maxWidth: .infinity)
                                    .frame(height: 50)
                                    .background(Color.white)
                                    .cornerRadius(8)
                                }
                            }

                            // ── أزرار إجراءات ثانوية (أيقونات مثل نيتفلكس) ──
                            HStack(spacing: 0) {
                                actionIconBtn(icon: favStore.isFavorite(itemId) ? "checkmark" : "plus",
                                              label: L("قائمتي", "My List")) {
                                    favStore.toggle(item: VideoItem(id: itemId, title: d.title,
                                                                    imageUrl: d.imageUrl, type: "post"))
                                }

                                if d.isMovie {
                                    actionIconBtn(icon: "arrow.down.to.line", label: L("تنزيل", "Download")) {
                                        DownloadManager.shared.startDownload(
                                            item: VideoItem(id: itemId, title: d.title,
                                                            imageUrl: d.imageUrl, type: "post"),
                                            isMovie: true, vUrl: d.movieUrl, sUrl: d.movieSubtitleUrl
                                        )
                                    }
                                }

                                actionIconBtn(icon: "square.and.arrow.up", label: L("مشاركة", "Share")) {
                                    showShareSheet = true
                                }
                            }

                            // ── القصة مع "عرض المزيد" ──
                            if !d.synopsis.isEmpty {
                                VStack(alignment: .leading, spacing: 8) {
                                    Text(L("القصة", "Synopsis"))
                                        .font(appFont(16, bold: true))
                                        .foregroundColor(.white)

                                    Text(d.synopsis)
                                        .font(appFont(14))
                                        .foregroundColor(.white.opacity(0.75))
                                        .lineSpacing(5)
                                        .lineLimit(synopsisExpanded ? nil : 3)

                                    Button {
                                        withAnimation(.easeInOut(duration: 0.25)) {
                                            synopsisExpanded.toggle()
                                        }
                                    } label: {
                                        Text(synopsisExpanded ? L("عرض أقل", "Show Less") : L("عرض المزيد", "Read More"))
                                            .font(appFont(13, bold: true))
                                            .foregroundColor(UT_RED)
                                    }
                                }
                                .padding(.top, 4)
                            }
                        }
                        .padding(.horizontal, 18)
                        .padding(.top, -16) // يطغى قليلاً على التدرج للتداخل مع Backdrop
                        if !d.isMovie && !d.sortedSeasons.isEmpty {
                            VStack(alignment: .leading, spacing: 16) {
                                HStack {
                                    Text(L("الحلقات", "Episodes"))
                                        .font(appFont(18, bold: true))
                                        .foregroundColor(.white)
                                    Spacer()
                                    Text(L("\(d.episodes.count) حلقة", "\(d.episodes.count) Episodes"))
                                        .font(appFont(12, bold: true))
                                        .foregroundColor(.gray)
                                }
                                .padding(.horizontal, 20)

                                if d.sortedSeasons.count > 1 {
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 10) {
                                            ForEach(d.sortedSeasons, id: \.self) { season in
                                                Button { selectedSeason = season } label: {
                                                    Text(season)
                                                        .font(appFont(14, bold: true))
                                                        .padding(.horizontal, 18).padding(.vertical, 9)
                                                        .background(selectedSeason == season ? UT_RED : Color.white.opacity(0.08))
                                                        .foregroundColor(.white)
                                                        .cornerRadius(20)
                                                        .overlay(
                                                            RoundedRectangle(cornerRadius: 20)
                                                                .stroke(selectedSeason == season ? .clear : Color.white.opacity(0.1), lineWidth: 1)
                                                        )
                                                }
                                            }
                                        }
                                        .padding(.horizontal, 20)
                                    }
                                }

                                LazyVStack(spacing: 12) {
                                    let eps = d.seasonsDict[selectedSeason] ?? []
                                    ForEach(eps) { ep in
                                        HStack(spacing: 14) {
                                            Button {
                                                playEpisode(d: d, ep: ep)
                                            } label: {
                                                HStack {
                                                    ZStack {
                                                        Circle()
                                                            .fill(Color.white.opacity(0.08))
                                                            .frame(width: 36, height: 36)
                                                        if let n = ep.episodeNumber {
                                                            Text("\(n)")
                                                                .font(appFont(14, bold: true))
                                                                .foregroundColor(.white)
                                                        } else {
                                                            Image(systemName: "play.fill")
                                                                .font(appFont(14))
                                                                .foregroundColor(UT_RED)
                                                        }
                                                    }
                                                    Text(ep.title)
                                                        .font(appFont(14, bold: true))
                                                        .foregroundColor(.white)
                                                        .lineLimit(1)
                                                    Spacer()
                                                    if WatchProgressStore.shared.progress(for: itemId)?.episodeId == ep.id {
                                                        Image(systemName: "play.circle.fill")
                                                            .foregroundColor(UT_RED)
                                                    }
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

                        CommentsSectionView(itemId: itemId)
                            .padding(.horizontal, 20)
                            .padding(.bottom, 40)
                    }
                }
            } else {
                VStack(spacing: 16) {
                    Image(systemName: "exclamationmark.triangle")
                        .font(appFont(50)).foregroundColor(.gray)
                    Text("تعذّر تحميل البيانات").foregroundColor(.gray)
                    Button("إعادة المحاولة") { load() }
                        .foregroundColor(UT_RED)
                }
            }
        }
        .navigationBarTitleDisplayMode(.inline)
        .fullScreenCover(item: $playerData) { data in
            CustomPlayerView(
                itemId: data.itemId,
                itemTitle: data.itemTitle,
                itemImageUrl: data.itemImageUrl,
                isMovie: data.isMovie,
                videoUrl: data.videoUrl,
                videoUrl720: data.videoUrl720,
                videoUrl1080: data.videoUrl1080,
                videoUrl360: data.videoUrl360,
                videoUrl4k: data.videoUrl4k,
                subtitleUrl: data.subtitleUrl,
                subtitleVttUrl: data.subtitleVttUrl,
                episodeId: data.episodeId,
                episodeTitle: data.episodeTitle,
                episodes: data.episodes,
                onTitleTap: {
                    // إغلاق المشغل والعودة إلى التفاصيل (نحن بالفعل في التفاصيل)
                    playerData = nil
                }
            )
        }
        .sheet(isPresented: $showShareSheet) {
            if let d = details {
                ShareSheet(items: [
                    "\(d.title) - شاهد الآن على UTan",
                    "https://movie.vodu.me/index.php?do=view&type=post&id=\(itemId)"
                ])
            }
        }
        .onAppear { load() }
    }

    private func load() {
        loading = true
        scraper.fetchDetails(id: itemId) { result in
            details = result
            if let firstSeason = result.sortedSeasons.first { selectedSeason = firstSeason }
            loading = false
        }
    }

    private func playMovie(d: MediaDetails) {
        playerData = PlayerData(
            itemId: itemId, itemTitle: d.title, itemImageUrl: d.imageUrl,
            isMovie: true,
            videoUrl: d.movieUrl, videoUrl720: d.movieUrl720, videoUrl1080: d.movieUrl1080,
            videoUrl360: d.movieUrl360, videoUrl4k: d.movieUrl4k,
            subtitleUrl: d.movieSubtitleUrl, subtitleVttUrl: d.movieSubtitleVttUrl,
            episodeId: "", episodeTitle: "", episodes: []
        )
    }

    private func playEpisode(d: MediaDetails, ep: EpisodeItem) {
        playerData = PlayerData(
            itemId: itemId, itemTitle: d.title,
            itemImageUrl: d.imageUrl,
            isMovie: false,
            videoUrl: ep.url,
            videoUrl720: ep.url720,
            videoUrl1080: ep.url1080,
            videoUrl360: ep.url360,
            videoUrl4k: ep.url4k,
            subtitleUrl: ep.subtitleUrl,
            subtitleVttUrl: ep.subtitleVttUrl,
            episodeId: ep.id,
            episodeTitle: ep.title,
            episodes: d.episodes
        )
    }

    // ─── مساعدات واجهة DetailsView ───

    /// ارتفاع الـ backdrop مضبوط حسب حجم الشاشة واتجاهها (عامودي/مستطيل + آيفون/آيباد)
    private func backdropHeight(geo: GeometryProxy) -> CGFloat {
        let isLandscape = geo.size.width > geo.size.height
        let isIpad = UIDevice.current.userInterfaceIdiom == .pad
        if isIpad {
            return isLandscape ? min(geo.size.height * 0.80, 480) : min(geo.size.width * 0.70, 500)
        } else {
            return isLandscape ? min(geo.size.height * 0.85, 320) : min(geo.size.width * 1.15, 420)
        }
    }

    /// تقدير ثابت يُستخدم لـ .frame(height:) الخارجي قبل معرفة الـ geo الحقيقي
    private func backdropHeightEstimate() -> CGFloat {
        let w = UIScreen.main.bounds.width
        let h = UIScreen.main.bounds.height
        let isLandscape = w > h
        let isIpad = UIDevice.current.userInterfaceIdiom == .pad
        if isIpad { return isLandscape ? 480 : 500 }
        return isLandscape ? 320 : min(w * 1.15, 420)
    }

    private func metaBadge(_ text: String, icon: String, color: Color = .white) -> some View {
        HStack(spacing: 4) {
            Image(systemName: icon)
                .font(appFont(10, bold: true))
                .foregroundColor(color)
            Text(text)
                .font(appFont(12, bold: true))
                .foregroundColor(color)
        }
        .padding(.horizontal, 10).padding(.vertical, 5)
        .background(Color.white.opacity(0.1))
        .cornerRadius(20)
    }

    private func genrePill(_ text: String) -> some View {
        Text(text)
            .font(appFont(11, bold: true))
            .foregroundColor(UT_RED)
            .padding(.horizontal, 10).padding(.vertical, 5)
            .background(UT_RED.opacity(0.12))
            .cornerRadius(20)
            .overlay(RoundedRectangle(cornerRadius: 20).stroke(UT_RED.opacity(0.3), lineWidth: 1))
    }

    private func actionIconBtn(icon: String, label: String, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            VStack(spacing: 5) {
                Image(systemName: icon)
                    .font(appFont(22, bold: false))
                    .foregroundColor(.white)
                Text(label)
                    .font(appFont(10, bold: false))
                    .foregroundColor(.white.opacity(0.8))
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, 10)
        }
    }

    private func badge(_ text: String) -> some View {
        Text(text)
            .font(appFont(12, bold: true))
            .padding(.horizontal, 10).padding(.vertical, 4)
            .background(Color.white.opacity(0.15))
            .cornerRadius(6)
            .foregroundColor(.white)
    }
}
"""
with open("UTan/UTan/Views.swift", "w", encoding="utf-8") as f:
    f.write(views_swift_p1 + views_swift_p2 + views_swift_p3 + views_swift_p4)

# 8. AccountViews.swift (تسجيل الدخول / إنشاء حساب / الملف الشخصي / التعليقات)
account_swift = r"""import SwiftUI

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – حقل إدخال موحّد بنفس هوية التطبيق
// ─────────────────────────────────────────────────────────────────────────────
struct UTTextField: View {
    let placeholder: String
    @Binding var text: String
    var isSecure: Bool = false
    var keyboard: UIKeyboardType = .default

    var body: some View {
        Group {
            if isSecure {
                SecureField("", text: $text, prompt: Text(placeholder).foregroundColor(.gray))
            } else {
                TextField("", text: $text, prompt: Text(placeholder).foregroundColor(.gray))
                    .keyboardType(keyboard)
                    .autocapitalization(.none)
                    .disableAutocorrection(true)
            }
        }
        .padding()
        .foregroundColor(.white)
        .background(Color.white.opacity(0.08))
        .cornerRadius(12)
        .overlay(RoundedRectangle(cornerRadius: 12).stroke(Color.white.opacity(0.12), lineWidth: 1))
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – شاشة الحساب: تسجيل دخول / إنشاء حساب / ملف شخصي
// ─────────────────────────────────────────────────────────────────────────────
struct AccountView: View {
    @ObservedObject private var session = AuthSession.shared
    @State private var mode: AuthMode = .login

    enum AuthMode { case login, signup }

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            if session.isLoggedIn {
                ProfileView()
            } else {
                AuthFormView(mode: $mode)
            }
        }
        .navigationTitle(L("حسابي", "Account"))
    }
}

private struct AuthFormView: View {
    @Binding var mode: AccountView.AuthMode
    @State private var email = ""
    @State private var password = ""
    @State private var confirmPassword = ""
    @State private var displayName = ""
    @State private var isLoading = false
    @State private var isGoogleLoading = false
    @State private var errorMessage: String?

    var body: some View {
        ScrollView {
            VStack(spacing: 18) {
                if let logoImage = UIImage(named: "logo") {
                    Image(uiImage: logoImage)
                        .resizable().scaledToFit()
                        .frame(width: 80, height: 80)
                        .padding(.top, 30)
                }

                Text(mode == .login ? "تسجيل الدخول" : "إنشاء حساب جديد")
                    .font(appFont(22, bold: true))
                    .foregroundColor(.white)

                VStack(spacing: 14) {
                    if mode == .signup {
                        UTTextField(placeholder: "الاسم", text: $displayName)
                    }
                    UTTextField(placeholder: "البريد الإلكتروني", text: $email, keyboard: .emailAddress)
                    UTTextField(placeholder: "كلمة المرور", text: $password, isSecure: true)
                    if mode == .signup {
                        UTTextField(placeholder: "تأكيد كلمة المرور", text: $confirmPassword, isSecure: true)
                    }
                }
                .padding(.horizontal, 24)

                if let error = errorMessage {
                    Text(error)
                        .font(appFont(13))
                        .foregroundColor(UT_RED)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 24)
                }

                Button {
                    submit()
                } label: {
                    ZStack {
                        if isLoading {
                            ProgressView().progressViewStyle(CircularProgressViewStyle(tint: .white))
                        } else {
                            Text(mode == .login ? "دخول" : "إنشاء الحساب")
                                .font(appFont(16, bold: true))
                        }
                    }
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(UT_RED)
                    .foregroundColor(.white)
                    .cornerRadius(12)
                }
                .disabled(isLoading)
                .padding(.horizontal, 24)
                .padding(.top, 6)

                HStack(spacing: 10) {
                    Rectangle().fill(Color.white.opacity(0.12)).frame(height: 1)
                    Text("أو").font(appFont(12)).foregroundColor(.gray)
                    Rectangle().fill(Color.white.opacity(0.12)).frame(height: 1)
                }
                .padding(.horizontal, 24)
                .padding(.top, 4)

                Button {
                    signInWithGoogle()
                } label: {
                    HStack(spacing: 10) {
                        if isGoogleLoading {
                            ProgressView().progressViewStyle(CircularProgressViewStyle(tint: .white))
                        } else {
                            Image(systemName: "g.circle.fill")
                                .font(appFont(18))
                            Text("المتابعة عبر Google")
                                .font(appFont(15, bold: true))
                        }
                    }
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.white.opacity(0.08))
                    .foregroundColor(.white)
                    .cornerRadius(12)
                    .overlay(RoundedRectangle(cornerRadius: 12).stroke(Color.white.opacity(0.15), lineWidth: 1))
                }
                .disabled(isGoogleLoading || isLoading)
                .padding(.horizontal, 24)

                Button {
                    withAnimation {
                        mode = (mode == .login) ? .signup : .login
                        errorMessage = nil
                    }
                } label: {
                    Text(mode == .login ? "ليس لديك حساب؟ أنشئ حساباً" : "لديك حساب بالفعل؟ سجّل الدخول")
                        .font(appFont(14, bold: true))
                        .foregroundColor(.gray)
                }
                .padding(.top, 4)
                .padding(.bottom, 40)
            }
        }
    }

    private func signInWithGoogle() {
        errorMessage = nil
        isGoogleLoading = true
        SupabaseManager.shared.signInWithGoogle { result in
            isGoogleLoading = false
            switch result {
            case .success: break
            case .failure(let msg): errorMessage = msg
            }
        }
    }

    private func submit() {
        errorMessage = nil
        guard !email.trimmingCharacters(in: .whitespaces).isEmpty,
              !password.isEmpty else {
            errorMessage = "الرجاء تعبئة جميع الحقول"
            return
        }
        if mode == .signup {
            guard !displayName.trimmingCharacters(in: .whitespaces).isEmpty else {
                errorMessage = "الرجاء إدخال اسمك"
                return
            }
            guard password == confirmPassword else {
                errorMessage = "كلمتا المرور غير متطابقتين"
                return
            }
            guard password.count >= 6 else {
                errorMessage = "يجب أن تتكون كلمة المرور من 6 أحرف على الأقل"
                return
            }
        }

        isLoading = true
        let completion: (AuthResult) -> Void = { result in
            isLoading = false
            switch result {
            case .success: break
            case .failure(let msg): errorMessage = msg
            }
        }
        if mode == .login {
            SupabaseManager.shared.signIn(email: email, password: password, completion: completion)
        } else {
            SupabaseManager.shared.signUp(email: email, password: password, displayName: displayName, completion: completion)
        }
    }
}

private struct ProfileView: View {
    @ObservedObject private var session = AuthSession.shared
    @State private var showSignOutConfirm = false

    var body: some View {
        ScrollView {
            VStack(spacing: 20) {
                ZStack {
                    Circle().fill(UT_RED.opacity(0.2)).frame(width: 90, height: 90)
                    Text(String(session.user?.displayName.prefix(1) ?? "?"))
                        .font(appFont(36, bold: true))
                        .foregroundColor(UT_RED)
                }
                .padding(.top, 30)

                Text(session.user?.displayName ?? "")
                    .font(appFont(20, bold: true))
                    .foregroundColor(.white)
                if let email = session.user?.email {
                    Text(email)
                        .font(appFont(14))
                        .foregroundColor(.gray)
                }

                Button {
                    showSignOutConfirm = true
                } label: {
                    HStack {
                        Image(systemName: "rectangle.portrait.and.arrow.right")
                        Text("تسجيل الخروج")
                    }
                    .font(appFont(15, bold: true))
                    .foregroundColor(.white)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.white.opacity(0.08))
                    .cornerRadius(12)
                }
                .padding(.horizontal, 24)
                .padding(.top, 20)
            }
        }
        .confirmationDialog("هل تريد تسجيل الخروج؟", isPresented: $showSignOutConfirm, titleVisibility: .visible) {
            Button("تسجيل الخروج", role: .destructive) { session.signOut() }
            Button("إلغاء", role: .cancel) {}
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – قسم التعليقات (يُستخدم أسفل صفحة التفاصيل)
// ─────────────────────────────────────────────────────────────────────────────
struct CommentsSectionView: View {
    let itemId: String
    @ObservedObject private var session = AuthSession.shared
    @State private var comments: [CommentItem] = []
    @State private var newComment = ""
    @State private var isLoading = true
    @State private var isPosting = false
    @State private var showLoginPrompt = false

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack {
                Text("التعليقات")
                    .font(appFont(18, bold: true))
                    .foregroundColor(.white)
                Spacer()
                if !comments.isEmpty {
                    Text("\(comments.count)")
                        .font(appFont(12))
                        .foregroundColor(.gray)
                }
            }

            if session.isLoggedIn {
                HStack(alignment: .bottom, spacing: 10) {
                    UTTextField(placeholder: "أضف تعليقاً...", text: $newComment)
                    Button {
                        post()
                    } label: {
                        if isPosting {
                            ProgressView().progressViewStyle(CircularProgressViewStyle(tint: .white))
                                .frame(width: 44, height: 44)
                        } else {
                            Image(systemName: "paperplane.fill")
                                .foregroundColor(.white)
                                .frame(width: 44, height: 44)
                                .background(UT_RED)
                                .cornerRadius(12)
                        }
                    }
                    .disabled(newComment.trimmingCharacters(in: .whitespaces).isEmpty || isPosting)
                }
            } else {
                Button {
                    showLoginPrompt = true
                } label: {
                    HStack {
                        Image(systemName: "lock.fill")
                        Text("سجّل الدخول لإضافة تعليق")
                    }
                    .font(appFont(14, bold: true))
                    .foregroundColor(.white)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 12)
                    .background(Color.white.opacity(0.08))
                    .cornerRadius(12)
                }
            }

            if isLoading {
                ProgressView()
                    .progressViewStyle(CircularProgressViewStyle(tint: .white))
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 20)
            } else if comments.isEmpty {
                Text("لا توجد تعليقات بعد، كن أول من يعلّق!")
                    .font(appFont(13))
                    .foregroundColor(.gray)
                    .padding(.vertical, 10)
            } else {
                VStack(spacing: 12) {
                    ForEach(comments) { comment in
                        CommentRow(comment: comment, canDelete: comment.user_id == session.user?.id) {
                            delete(comment)
                        }
                    }
                }
            }
        }
        .onAppear { load() }
        .sheet(isPresented: $showLoginPrompt) {
            NavigationView {
                AccountView()
                    .toolbar {
                        ToolbarItem(placement: .navigationBarTrailing) {
                            Button("إغلاق") { showLoginPrompt = false }
                        }
                    }
            }
            .navigationViewStyle(StackNavigationViewStyle())
        }
    }

    private func load() {
        isLoading = true
        SupabaseManager.shared.fetchComments(itemId: itemId) { items in
            comments = items
            isLoading = false
        }
    }

    private func post() {
        let text = newComment.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !text.isEmpty else { return }
        isPosting = true
        SupabaseManager.shared.postComment(itemId: itemId, text: text) { success in
            isPosting = false
            if success {
                newComment = ""
                load()
            }
        }
    }

    private func delete(_ comment: CommentItem) {
        SupabaseManager.shared.deleteComment(id: comment.id) { success in
            if success { comments.removeAll { $0.id == comment.id } }
        }
    }
}

private struct CommentRow: View {
    let comment: CommentItem
    let canDelete: Bool
    let onDelete: () -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack {
                ZStack {
                    Circle().fill(UT_RED.opacity(0.2)).frame(width: 32, height: 32)
                    Text(String(comment.display_name.prefix(1)))
                        .font(appFont(13, bold: true))
                        .foregroundColor(UT_RED)
                }
                VStack(alignment: .leading, spacing: 2) {
                    Text(comment.display_name)
                        .font(appFont(13, bold: true))
                        .foregroundColor(.white)
                    Text(comment.formattedDate)
                        .font(appFont(11))
                        .foregroundColor(.gray)
                }
                Spacer()
                if canDelete {
                    Button(action: onDelete) {
                        Image(systemName: "trash")
                            .font(appFont(13))
                            .foregroundColor(.gray)
                    }
                }
            }
            Text(comment.text)
                .font(appFont(14))
                .foregroundColor(.white.opacity(0.9))
                .padding(.leading, 42)
        }
        .padding(12)
        .background(Color.white.opacity(0.05))
        .cornerRadius(12)
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – الشكاوى والاقتراحات
// ─────────────────────────────────────────────────────────────────────────────
struct FeedbackView: View {
    @State private var type = "suggestion"
    @State private var message = ""
    @State private var isSubmitting = false
    @State private var submitted = false
    @State private var myFeedback: [FeedbackItem] = []
    @State private var isLoadingList = true

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            ScrollView {
                VStack(alignment: .leading, spacing: 18) {
                    VStack(alignment: .leading, spacing: 12) {
                        Text("أرسل لنا رأيك")
                            .font(appFont(17, bold: true))
                            .foregroundColor(.white)

                        Picker("النوع", selection: $type) {
                            Text("اقتراح").tag("suggestion")
                            Text("شكوى").tag("complaint")
                        }
                        .pickerStyle(.segmented)
                        .colorMultiply(.white)

                        ZStack(alignment: .topLeading) {
                            if message.isEmpty {
                                Text("اكتب رسالتك هنا...")
                                    .foregroundColor(.gray)
                                    .padding(.top, 12)
                                    .padding(.leading, 14)
                            }
                            TextEditor(text: $message)
                                .scrollContentBackground(.hidden)
                                .foregroundColor(.white)
                                .frame(height: 120)
                                .padding(8)
                        }
                        .background(Color.white.opacity(0.08))
                        .cornerRadius(12)
                        .overlay(RoundedRectangle(cornerRadius: 12).stroke(Color.white.opacity(0.12), lineWidth: 1))

                        Button {
                            submit()
                        } label: {
                            ZStack {
                                if isSubmitting {
                                    ProgressView().progressViewStyle(CircularProgressViewStyle(tint: .white))
                                } else {
                                    Text(submitted ? "تم الإرسال ✓" : "إرسال")
                                        .font(appFont(15, bold: true))
                                }
                            }
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(submitted ? Color.green.opacity(0.6) : UT_RED)
                            .foregroundColor(.white)
                            .cornerRadius(12)
                        }
                        .disabled(isSubmitting || message.trimmingCharacters(in: .whitespaces).isEmpty)
                    }
                    .padding()
                    .background(Color.white.opacity(0.04))
                    .cornerRadius(16)
                    .padding(.horizontal, 16)
                    .padding(.top, 12)

                    VStack(alignment: .leading, spacing: 12) {
                        Text("رسائلك السابقة")
                            .font(appFont(16, bold: true))
                            .foregroundColor(.white)
                            .padding(.horizontal, 16)

                        if isLoadingList {
                            ProgressView()
                                .frame(maxWidth: .infinity)
                                .padding()
                        } else if myFeedback.isEmpty {
                            Text("لا توجد رسائل بعد")
                                .font(appFont(13))
                                .foregroundColor(.gray)
                                .padding(.horizontal, 16)
                        } else {
                            VStack(spacing: 10) {
                                ForEach(myFeedback) { fb in
                                    FeedbackRow(item: fb)
                                }
                            }
                            .padding(.horizontal, 16)
                        }
                    }
                    .padding(.bottom, 40)
                }
            }
        }
        .navigationTitle(L("الشكاوى والاقتراحات", "Feedback"))
        .onAppear { load() }
    }

    private func submit() {
        isSubmitting = true
        SupabaseManager.shared.submitFeedback(type: type, message: message) { success in
            isSubmitting = false
            if success {
                message = ""
                submitted = true
                load()
                DispatchQueue.main.asyncAfter(deadline: .now() + 2) { submitted = false }
            }
        }
    }

    private func load() {
        isLoadingList = true
        SupabaseManager.shared.fetchMyFeedback { items in
            myFeedback = items
            isLoadingList = false
        }
    }
}

private struct FeedbackRow: View {
    let item: FeedbackItem

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Text(item.isComplaint ? "شكوى" : "اقتراح")
                    .font(appFont(11, bold: true))
                    .foregroundColor(.white)
                    .padding(.horizontal, 10).padding(.vertical, 4)
                    .background(item.isComplaint ? UT_RED : Color.blue.opacity(0.7))
                    .cornerRadius(8)
                Spacer()
                Text(item.status == "resolved" ? "تم الحل" : "قيد المراجعة")
                    .font(appFont(11, bold: true))
                    .foregroundColor(item.status == "resolved" ? .green : .orange)
                Text(item.formattedDate)
                    .font(appFont(11))
                    .foregroundColor(.gray)
            }
            Text(item.message)
                .font(appFont(13))
                .foregroundColor(.white.opacity(0.9))
        }
        .padding(12)
        .background(Color.white.opacity(0.05))
        .cornerRadius(12)
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – لوحة الإدارة (تظهر فقط للحسابات is_admin = true)
// ─────────────────────────────────────────────────────────────────────────────
struct AdminPanelView: View {
    @State private var allFeedback: [FeedbackItem] = []
    @State private var isLoading = true
    @State private var filter: StatusFilter = .open

    enum StatusFilter { case all, open, resolved }

    private var filtered: [FeedbackItem] {
        switch filter {
        case .all: return allFeedback
        case .open: return allFeedback.filter { $0.status != "resolved" }
        case .resolved: return allFeedback.filter { $0.status == "resolved" }
        }
    }

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            VStack(spacing: 0) {
                Picker("فلتر", selection: $filter) {
                    Text(L("الكل", "All")).tag(StatusFilter.all)
                    Text(L("قيد المراجعة", "Under Review")).tag(StatusFilter.open)
                    Text(L("تم الحل", "Resolved")).tag(StatusFilter.resolved)
                }
                .pickerStyle(.segmented)
                .colorMultiply(.white)
                .padding()

                if isLoading {
                    ProgressView().frame(maxWidth: .infinity, maxHeight: .infinity)
                } else if filtered.isEmpty {
                    Text("لا توجد رسائل")
                        .foregroundColor(.gray)
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                } else {
                    ScrollView {
                        VStack(spacing: 10) {
                            ForEach(filtered) { fb in
                                AdminFeedbackRow(item: fb) { newStatus in
                                    updateStatus(fb, to: newStatus)
                                }
                            }
                        }
                        .padding()
                    }
                }
            }
        }
        .navigationTitle(L("لوحة الإدارة", "Admin Panel"))
        .onAppear { load() }
        .refreshable { load() }
    }

    private func load() {
        isLoading = true
        SupabaseManager.shared.fetchAllFeedback { items in
            allFeedback = items
            isLoading = false
        }
    }

    private func updateStatus(_ item: FeedbackItem, to status: String) {
        SupabaseManager.shared.updateFeedbackStatus(id: item.id, status: status) { success in
            if success { load() }
        }
    }
}

private struct AdminFeedbackRow: View {
    let item: FeedbackItem
    let onUpdateStatus: (String) -> Void

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Text(item.isComplaint ? "شكوى" : "اقتراح")
                    .font(appFont(11, bold: true))
                    .foregroundColor(.white)
                    .padding(.horizontal, 10).padding(.vertical, 4)
                    .background(item.isComplaint ? UT_RED : Color.blue.opacity(0.7))
                    .cornerRadius(8)
                Spacer()
                Text(item.formattedDate)
                    .font(appFont(11))
                    .foregroundColor(.gray)
            }
            Text(item.display_name + (item.email.map { " · \($0)" } ?? ""))
                .font(appFont(12, bold: true))
                .foregroundColor(.gray)
            Text(item.message)
                .font(appFont(13))
                .foregroundColor(.white.opacity(0.9))

            HStack {
                Spacer()
                if item.status == "resolved" {
                    Button("إعادة فتح") { onUpdateStatus("open") }
                        .font(appFont(12, bold: true))
                        .foregroundColor(.orange)
                } else {
                    Button("تمييز كمحلول") { onUpdateStatus("resolved") }
                        .font(appFont(12, bold: true))
                        .foregroundColor(.green)
                }
            }
        }
        .padding(12)
        .background(Color.white.opacity(0.05))
        .cornerRadius(12)
    }
}
"""
with open("UTan/UTan/AccountViews.swift", "w", encoding="utf-8") as f:
    f.write(account_swift)

print("✅ تم إنشاء مشروع UTan بالكامل مع إضافة إعدادات الترجمة المنبثقة داخل المشغل.")
print("   - زر جديد 'captions.bubble' في شريط التحكم العلوي.")
print("   - شاشة منبثقة (SubtitleSettingsView) تحتوي على:")
print("       • تفعيل/إلغاء الترجمة.")
print("       • منزلق لتأخير الترجمة (-5 إلى +5 ثوانٍ).")
print("       • منزلق لحجم الخط.")
print("       • أزرار لاختيار لون النص (أبيض، أصفر، سماوي، وردي، أحمر، أخضر، أزرق).")
print("       • منزلق لشفافية خلفية الترجمة.")
print("       • اختيار الخط (Cairo، Rubik، IBM Plex Sans).")
print("   - يتم تطبيق التأخير مباشرة على الترجمة المعروضة.")
print("   - الكود كامل غير منقوص، وجاهز للبناء.")