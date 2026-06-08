import os

# Create directory structure
os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# 1. Write project.pbxproj
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

# 2. Write Info.plist
info_plist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
\t<key>CFBundleDevelopmentRegion</key>
\t<string>en</string>
\t<key>CFBundleExecutable</key>
\t<string>$(EXECUTABLE_NAME)</string>
\t<key>CFBundleIdentifier</key>
\t<string>com.mustaqil.utan</string>
\t<key>CFBundleInfoDictionaryVersion</key>
\t<string>6.0</string>
\t<key>CFBundleName</key>
\t<string>UTan</string>
\t<key>CFBundlePackageType</key>
\t<string>APPL</string>
\t<key>CFBundleShortVersionString</key>
\t<string>4.0</string>
\t<key>CFBundleVersion</key>
\t<string>4</string>
\t<key>LSRequiresIPhoneOS</key>
\t<true/>
\t<key>NSAppTransportSecurity</key>
\t<dict>
\t\t<key>NSAllowsArbitraryLoads</key>
\t\t<true/>
\t</dict>
\t<key>UIBackgroundModes</key>
\t<array>
\t\t<string>fetch</string>
\t\t<string>processing</string>
\t</array>
\t<key>UILaunchScreen</key>
\t<dict/>
\t<key>UISupportedInterfaceOrientations</key>
\t<array>
\t\t<string>UIInterfaceOrientationPortrait</string>
\t\t<string>UIInterfaceOrientationLandscapeLeft</string>
\t\t<string>UIInterfaceOrientationLandscapeRight</string>
\t</array>
\t<key>UIUserInterfaceStyle</key>
\t<string>Dark</string>
</dict>
</plist>
"""

with open("UTan/UTan/Info.plist", "w", encoding="utf-8") as f:
    f.write(info_plist)

# 3. Write UTanApp.swift
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

# 4. Write Scraper.swift
# NOTE: UT_RED is completely removed. All accent usage replaced with UT_WHITE / APP_BG.
scraper_swift = r"""import Foundation
import SwiftUI

// ─────────────────────────────────────────────
// MARK: – Global Colors & Configs
// ─────────────────────────────────────────────

/// Deep dark purple — primary background / surface colour.
let APP_BG     = Color(red: 0.05, green: 0.02, blue: 0.09)

/// Pure white — used for all interactive icons, primary text, and accent elements.
let UT_WHITE   = Color.white

/// Subtle highlight surface (white at low opacity).
let UT_SURFACE = Color.white.opacity(0.12)

class AppSettings: ObservableObject {
    static let shared = AppSettings()

    @AppStorage("sub_fontSize")   var subtitleFontSize: Double  = 22.0
    @AppStorage("sub_colorHex")   var subtitleColorHex: String  = "#FFFFFF"
    @AppStorage("sub_bgOpacity")  var subtitleBgOpacity: Double = 0.6
    @AppStorage("sub_bottomPad")  var subtitleBottomPad: Double = 60.0
    @AppStorage("sub_enabled")    var subtitlesEnabled: Bool    = true

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
              videoUrl: String, videoUrl1080: String, videoUrl360: String,
              subUrl: String, subVttUrl: String) {
        let record = WatchProgress(
            itemId: itemId, title: title, imageUrl: imageUrl,
            episodeId: episodeId, episodeTitle: episodeTitle,
            progressSeconds: progress, durationSeconds: duration,
            updatedAt: Date(),
            videoUrl: videoUrl, videoUrl1080: videoUrl1080, videoUrl360: videoUrl360,
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
// MARK: – Main scraper / network layer
// ─────────────────────────────────────────────

class MovieScraper: ObservableObject {
    @Published var heroItems: [VideoItem] = []
    @Published var categories: [(name: String, items: [VideoItem])] = []
    @Published var allItemsPool: [VideoItem] = []
    @Published var isLoading = false

    let baseUrl = "https://movie.vodu.me/"

    // أقسام الصفحة الرئيسية المستخرجة من الموقع مباشرة (لضمان ظهورها)
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
    
    URLSession.shared.dataTask(with: request) { data, _, _ in
        guard let data = data, let html = String(data: data, encoding: .utf8) else {
            DispatchQueue.main.async { self.isLoading = false }
            return
        }
        let (carouselItems, _) = Self.parseHome(html: html, base: self.baseUrl)
        
        DispatchQueue.main.async {
            self.heroItems = carouselItems
            
            // 1. نضيف "الرائج الآن" فوراً من carouselItems (حتى قبل تحميل الأقسام الأخرى)
            var allCategories: [(name: String, items: [VideoItem])] = []
            if !carouselItems.isEmpty {
                let trendingItems = Array(carouselItems.prefix(10))
                allCategories.append(("الرائج الآن", trendingItems))
            }
            
            // 2. نبدأ بتحميل الأقسام الأخرى في الخلفية
            let group = DispatchGroup()
            var tempSections: [(name: String, items: [VideoItem])] = []
            
            for section in self.homeSections {
                group.enter()
                self.fetchCategory(typeId: section.tagId, page: 1, useTag: true) { items, success in
                    if success && !items.isEmpty {
                        let topItems = Array(items.prefix(12))
                        tempSections.append((name: section.name, items: topItems))
                    } else {
                        print("⚠️ فشل أو قسم فارغ: \(section.name) (tag \(section.tagId))")
                    }
                    group.leave()
                }
            }
            
            group.notify(queue: .main) {
                // نضيف الأقسام التي تم تحميلها بنجاح
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
        
        URLSession.shared.dataTask(with: request) { data, _, _ in
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

    // MARK: – HTML parsers (static)

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
        
        // لا نحتاج لاستخراج الأقسام من HTML لأننا نستخدم homeSections الثابتة
        // لكن نترك الدالة كما هي للاستخدام المستقبلي إن لزم الأمر
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
                        items.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
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
                    let fakeId = "home_\(items.count)_\(title.prefix(10))"
                    items.append(VideoItem(id: fakeId, title: title, imageUrl: img, type: "post"))
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
                    let epUrl360 = extract(url360Pattern, from: block)
                    let epUrl1080 = extract(url1080Pattern, from: block)
                    let epSrt    = extract(srtPattern, from: block)
                    let epWebvtt = extract(webvttPattern, from: block)

                    if !epUrl.isEmpty {
                        parsedEpisodes.append(EpisodeItem(
                            id: epId,
                            title: epTitle.isEmpty ? "الحلقة \(parsedEpisodes.count + 1)" : epTitle,
                            url: epUrl,
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
            let moviePattern = #"data-url="([^"]+)"[^>]*data-url360="([^"]*)"[^>]*data-url1080="([^"]*)"[^>]*data-srt="([^"]*)"[^>]*data-webvtt="([^"]*)""#
            if let rx = try? NSRegularExpression(pattern: moviePattern, options: [.dotMatchesLineSeparators]),
               let m = rx.firstMatch(in: html, range: NSRange(html.startIndex..., in: html)),
               m.numberOfRanges >= 6 {
                if let r = Range(m.range(at: 1), in: html) { d.movieUrl           = String(html[r]) }
                if let r = Range(m.range(at: 2), in: html) { d.movieUrl360        = String(html[r]) }
                if let r = Range(m.range(at: 3), in: html) { d.movieUrl1080       = String(html[r]) }
                if let r = Range(m.range(at: 4), in: html) { d.movieSubtitleUrl   = String(html[r]) }
                if let r = Range(m.range(at: 5), in: html) { d.movieSubtitleVttUrl = String(html[r]) }
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

# 5. Write SubtitleParser.swift  (unchanged — no color references)
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

# 6. Write CustomPlayer.swift
# Changes:
#   - UT_RED removed from ALL player UI elements.
#   - Logo image asset replaces plain "UTan" watermark text.
#   - Speed indicator background: dark surface instead of red.
#   - Seek slider accent: white instead of red.
#   - Play/pause button: white circle on dark fill instead of red.
#   - Lock button active state: white instead of red.
#   - Quality selector active state: white surface instead of red.
#   - Error message background: dark surface instead of red.
#   - Loading close button: dark surface instead of red.
player_swift = r"""import SwiftUI
import AVKit
import AVFoundation

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

struct VideoPlayerView: UIViewControllerRepresentable {
    let player: AVPlayer
    let gravity: AVLayerVideoGravity
    let onTap: () -> Void
    let onLongPressBegan: () -> Void
    let onLongPressEnded: () -> Void

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
        let longPress = UILongPressGestureRecognizer(target: context.coordinator,
                                                     action: #selector(Coordinator.handleLongPress))
        longPress.minimumPressDuration = 0.4
        overlay.addGestureRecognizer(tap)
        overlay.addGestureRecognizer(longPress)

        // Logo watermark — uses logo.png bundled asset
        if let logoImage = UIImage(named: "logo") {
            let watermark = UIImageView(image: logoImage)
            watermark.alpha = 0.35
            watermark.contentMode = .scaleAspectFit
            watermark.frame = CGRect(x: 12, y: 46, width: 72, height: 28)
            watermark.autoresizingMask = [.flexibleRightMargin, .flexibleBottomMargin]
            vc.view.addSubview(watermark)
        } else {
            // Fallback text watermark if asset not yet loaded in simulator
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
                    onLongPressEnded: onLongPressEnded)
    }

    class Coordinator: NSObject {
        let onTap: () -> Void
        let onLongPressBegan: () -> Void
        let onLongPressEnded: () -> Void
        init(onTap: @escaping () -> Void,
             onLongPressBegan: @escaping () -> Void,
             onLongPressEnded: @escaping () -> Void) {
            self.onTap = onTap
            self.onLongPressBegan = onLongPressBegan
            self.onLongPressEnded = onLongPressEnded
        }
        @objc func handleTap() { onTap() }
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

    private var subtitleFont: Font {
        if let customFont = UIFont(name: "Cairo", size: CGFloat(settings.subtitleFontSize)) {
            return Font(customFont)
        }
        return .system(size: CGFloat(settings.subtitleFontSize), weight: .bold, design: .rounded)
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
                    }
                )
                .ignoresSafeArea()

                // ── 2× Speed indicator (no red — uses dark surface)
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

                // ── Subtitles
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

                // ── Error message
                if let error = errorMessage {
                    VStack {
                        Text(error)
                            .foregroundColor(.white)
                            .padding()
                            .background(Color.white.opacity(0.15))
                            .cornerRadius(8)
                    }
                }

                // ── Controls overlay
                if showControls || isLocked {
                    controlsOverlay(player: player)
                        .transition(.opacity)
                        .animation(.easeInOut(duration: 0.25), value: showControls)
                }

            } else {
                // ── Loading state
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

    // MARK: – Controls Overlay
    @ViewBuilder
    private func controlsOverlay(player: AVPlayer) -> some View {
        VStack {
            // ── Top bar
            HStack {
                if !isLocked {
                    Button { shutdown(); presentation.wrappedValue.dismiss() } label: {
                        Image(systemName: "arrow.backward").playerBtn()
                    }
                    Spacer()
                    // Logo in player header
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
                    // Lock active = white tint; inactive = white tint
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

            // ── Bottom controls
            if !isLocked {
                VStack(spacing: 12) {
                    // Seek bar — accent white
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
                        .accentColor(.white)
                        Text(formatTime(duration))
                            .timeLabel()
                    }
                    .padding(.horizontal, 16)

                    // Playback controls — play/pause: white on dark
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
                                .font(.system(size: 66))
                                .foregroundColor(.white)
                                .background(Circle().fill(Color.white.opacity(0.15)))
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

                    // Quality selector — active: white surface
                    HStack(spacing: 6) {
                        ForEach(VideoQuality.allCases) { q in
                            Button(q.rawValue) { switchQuality(to: q) }
                                .font(.system(size: 12, weight: quality == q ? .bold : .regular))
                                .foregroundColor(.white)
                                .padding(.horizontal, 10).padding(.vertical, 6)
                                .background(quality == q ? Color.white.opacity(0.25) : Color.clear)
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

    // MARK: – Player Setup
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
        case .q360:  return fixUrl(videoUrl360.isEmpty  ? videoUrl : videoUrl360)
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

# 7. Write Views.swift
# Changes:
#   - UT_RED removed from ALL views — replaced with UT_WHITE / UT_SURFACE / .white.
#   - HomeView: logo.png replaces plain "UTAN" text in floating header.
#   - HomeView: Network Navigation Cards row (Netflix/Anime/Kids/Hbo/Disney/Marvel)
#     inserted between History row and content category rows.
#   - History/Continue Watching row: conditionally shown only when items exist (unchanged).
#   - HeroBanner: Watch button uses white background with dark text.
#   - DetailsView: season selector, play button, episode rows all use white accent.
#   - UTanLoader spinner: white instead of red.
#   - PosterCard: progress bar accent white.
#   - BrowseView category cards: icon white instead of red.
#   - SettingsView: section headers, sliders, accent all white.
#   - DownloadsView: progress bar white.
#   - The old duplicate category-banner section that previously appeared below the
#     "Documentary / وثائقي" row is completely removed by not re-generating it.
views_swift = r"""import SwiftUI

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Loader  (spinner: white, no red)
// ─────────────────────────────────────────────────────────────────────────────
struct UTanLoader: View {
    @State private var spin = false
    var body: some View {
        VStack(spacing: 12) {
            ZStack {
                Circle()
                    .stroke(Color.white.opacity(0.2), lineWidth: 5)
                    .frame(width: 64, height: 64)
                Circle()
                    .trim(from: 0, to: 0.72)
                    .stroke(Color.white,
                            style: StrokeStyle(lineWidth: 5, lineCap: .round))
                    .frame(width: 64, height: 64)
                    .rotationEffect(.degrees(spin ? 360 : 0))
                    .animation(.linear(duration: 0.9).repeatForever(autoreverses: false),
                               value: spin)
            }
            .onAppear { spin = true }
            Text("UTAN")
                .font(.system(.caption, design: .monospaced))
                .foregroundColor(.white.opacity(0.7))
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
    let videoUrl1080: String
    let videoUrl360: String
    let subtitleUrl: String
    let subtitleVttUrl: String
    let episodeId: String
    let episodeTitle: String
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Poster Card  (progress bar accent: white)
// ─────────────────────────────────────────────────────────────────────────────
struct PosterCard: View {
    let item: VideoItem
    var progress: WatchProgress? = nil

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            ZStack(alignment: .bottom) {
                AsyncImage(url: URL(string: item.imageUrl)) { img in
                    img.resizable().aspectRatio(contentMode: .fill)
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
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – MainTabView  (accent: white, no red)
// ─────────────────────────────────────────────────────────────────────────────
struct MainTabView: View {
    @StateObject private var scraper = MovieScraper()

    var body: some View {
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
        .accentColor(.white)
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

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Network Navigation Card  (rectangular image card)
// ─────────────────────────────────────────────────────────────────────────────
/// Maps a bundled image asset name to the corresponding SiteCategory id so that
/// tapping a network card navigates directly to that category list.
struct NetworkCard: Identifiable {
    let id = UUID()
    let assetName: String   // Name of the bundled .jpg / .png image
    let label: String       // Display label shown below the image
    let categoryId: Int     // SiteCategory.id to link to
}

private let networkCards: [NetworkCard] = [
    NetworkCard(assetName: "Netflix",  label: "نتفليكس",  categoryId: 44),   // تم التعديل إلى 44
    NetworkCard(assetName: "Anime",    label: "أنمي",      categoryId: 2),    // كما هي
    NetworkCard(assetName: "Kids",     label: "أطفال",     categoryId: 9018), // تم التعديل لمنع تداخل الأفلام الأجنبية
    NetworkCard(assetName: "Hbo",      label: "HBO",        categoryId: 73),   // تم التعديل إلى 73
    NetworkCard(assetName: "Disney",   label: "ديزني",     categoryId: 72),   // تم التعديل إلى 72
    NetworkCard(assetName: "Marvel",   label: "مارفل",     categoryId: 9014)  // تم التعديل لمنع تداخل الأفلام التركية
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
                HStack(spacing: 14) {
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
        ZStack(alignment: .bottom) {
            // محاولة تحميل الصورة من المسار المباشر
            if let path = Bundle.main.path(forResource: card.assetName, ofType: "jpg"),
               let uiImage = UIImage(contentsOfFile: path) {
                Image(uiImage: uiImage)
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .frame(width: 140, height: 86)
                    .clipped()
                    .cornerRadius(14)
            } else if let path = Bundle.main.path(forResource: card.assetName, ofType: "png"),
                      let uiImage = UIImage(contentsOfFile: path) {
                Image(uiImage: uiImage)
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .frame(width: 140, height: 86)
                    .clipped()
                    .cornerRadius(14)
            } else {
                // خلفية رمادية مع النص
                RoundedRectangle(cornerRadius: 14)
                    .fill(Color.white.opacity(0.12))
                    .frame(width: 140, height: 86)
                    .overlay(
                        Text(card.label)
                            .font(.system(size: 15, weight: .bold))
                            .foregroundColor(.white)
                    )
            }
            
            // التدرج السفلي
            LinearGradient(colors: [.clear, .black.opacity(0.72)],
                           startPoint: .center, endPoint: .bottom)
                .cornerRadius(14)
                .frame(width: 140, height: 86)
            
            Text(card.label)
                .font(.system(size: 13, weight: .bold))
                .foregroundColor(.white)
                .padding(.bottom, 8)
        }
        .frame(width: 140, height: 86)
        .shadow(color: .black.opacity(0.45), radius: 6, x: 0, y: 3)
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – HomeView  (re-architected hierarchy + logo.png branding)
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
                    UTanLoader().frame(maxHeight: .infinity)
                } else {
                    ScrollView(showsIndicators: false) {
                        VStack(spacing: 0) {

                            // ── 1. HERO SECTION ────────────────────────────
                            if !scraper.heroItems.isEmpty {
                                HeroBanner(items: scraper.heroItems, scraper: scraper)
                                    .frame(height: UIScreen.main.bounds.height * 0.75)
                            }

                            VStack(alignment: .leading, spacing: 30) {

                                // ── 2. HISTORY / CONTINUE WATCHING ──────────
                                // Shown only when there is active watch history.
                                if !progressStore.recent.isEmpty {
                                    ContinueWatchingRow(items: progressStore.recent,
                                                        playItem: $playItem)
                                        .padding(.top, -60)  // Overlap hero bottom
                                        .zIndex(1)
                                }

                                // ── 3. NETWORK NAVIGATION CARDS ─────────────
                                // Horizontal row of rectangular branded cards.
                                NetworkCardsRow(scraper: scraper)

                                // ── 4. CONTENT ROWS (CATEGORIES) ────────────
                                // Dynamic sections scraped from the home page.
                                // The old duplicate section that appeared below
                                // the Documentary (وثائقي) row has been removed
                                // entirely — no redundant banner cards are rendered.
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

                // ── Floating header — logo.png branding ────────────────────
                // Floating header — logo.png branding
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
            }
            .navigationBarHidden(true)
            .fullScreenCover(item: $playItem) { data in
                CustomPlayerView(
                    itemId: data.itemId,
                    itemTitle: data.itemTitle,
                    itemImageUrl: data.itemImageUrl,
                    videoUrl: data.videoUrl,
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
// MARK: – Hero Banner  (Watch button: white bg + dark text; no red)
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

                    // Smooth bottom fade into APP_BG
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
                            // Watch button — pure white background, dark foreground
                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                HStack {
                                    Image(systemName: "play.fill")
                                    Text("شاهد الآن")
                                }
                                .font(.system(size: 16, weight: .bold))
                                .padding(.horizontal, 30).padding(.vertical, 12)
                                .background(Color.white)
                                .foregroundColor(Color(red: 0.05, green: 0.02, blue: 0.09))
                                .cornerRadius(12)
                            }

                            // Favourite button — white icons
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
// MARK: – Continue Watching Row  (progress bar: white; no red)
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

                                    // Progress bar — white accent
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
// MARK: – Browse & Category Lists  (icon: white; no red)
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
                            NavigationLink(destination: CategoryListView(category: cat,
                                                                         scraper: scraper)) {
                                ZStack {
                                    RoundedRectangle(cornerRadius: 16)
                                        .fill(Color.white.opacity(0.06))
                                    VStack(spacing: 8) {
                                        Image(systemName: "film")
                                            .font(.title2)
                                            .foregroundColor(.white)
                                        Text(cat.nameAr)
                                            .font(.system(size: 14, weight: .bold))
                                            .foregroundColor(.white)
                                    }
                                    .padding(10)
                                }
                                .frame(height: 100)
                            }
                        }
                    }
                    .padding()
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
                if loading { UTanLoader().padding() }
            }
        }
        .navigationTitle(category.nameAr)
        .onAppear { if items.isEmpty { loadMore() } }
    }

    private func loadMore() {
    loading = true
    // هنا نمرر remoteId بدلاً من id، ونمرر خيار استخدام الـ Tag
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
// MARK: – Downloads & Settings Views  (accent/progress: white; no red)
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
                                        // Progress bar: white tint
                                        ProgressView(value: dl.progress).tint(.white)
                                        Text("\(Int(dl.progress * 100))%")
                                            .font(.caption).foregroundColor(.gray)
                                    }
                                }
                                Spacer()
                                Button { manager.cancel(id: dl.id) } label: {
                                    Image(systemName: "xmark.circle.fill")
                                        .foregroundColor(.white.opacity(0.6))
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
                    // Section headers: white; sliders: white accent
                    Section(header: Text("إعدادات الترجمة").foregroundColor(.white)) {
                        Toggle("تفعيل الترجمة", isOn: $settings.subtitlesEnabled)
                        if settings.subtitlesEnabled {
                            VStack(alignment: .leading) {
                                Text("حجم الخط: \(Int(settings.subtitleFontSize))")
                                Slider(value: $settings.subtitleFontSize, in: 14...40, step: 1)
                                    .accentColor(.white)
                            }
                            VStack(alignment: .leading) {
                                Text("الهامش السفلي: \(Int(settings.subtitleBottomPad))")
                                Slider(value: $settings.subtitleBottomPad, in: 20...150, step: 5)
                                    .accentColor(.white)
                            }
                            VStack(alignment: .leading) {
                                Text("شفافية الخلفية: \(Int(settings.subtitleBgOpacity * 100))%")
                                Slider(value: $settings.subtitleBgOpacity, in: 0.0...1.0, step: 0.1)
                                    .accentColor(.white)
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

                    Section(header: Text("البيانات").foregroundColor(.white)) {
                        NavigationLink(destination: HistoryListView(store: historyStore)) {
                            Text("سجل المشاهدة (\(historyStore.recent.count))")
                        }
                        Button {
                            settings.clearCache()
                            cacheCleared = true
                            DispatchQueue.main.asyncAfter(deadline: .now() + 2) { cacheCleared = false }
                        } label: {
                            Text(cacheCleared ? "تم المسح!" : "مسح التخزين المؤقت والسجل")
                                .foregroundColor(.white.opacity(0.7))
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
// MARK: – DetailsView  (season selector / play button / episode rows: white; no red)
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
                UTanLoader()
            } else if let d = details {
                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 0) {

                        // ── Hero image + info overlay
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

                                // Action buttons — white fills, no red
                                HStack(spacing: 16) {
                                    if d.isMovie {
                                        // Primary play button: white bg + dark text
                                        Button { playMovie(d: d) } label: {
                                            HStack {
                                                Image(systemName: "play.fill")
                                                Text("شاهد الآن")
                                            }
                                            .font(.system(size: 16, weight: .bold))
                                            .frame(maxWidth: .infinity)
                                            .padding()
                                            .background(Color.white)
                                            .foregroundColor(Color(red: 0.05, green: 0.02, blue: 0.09))
                                            .cornerRadius(12)
                                        }

                                        // Download button
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

                                    // Favourite button
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

                        // ── Synopsis
                        if !d.synopsis.isEmpty {
                            VStack(alignment: .leading, spacing: 8) {
                                Text("القصة")
                                    .font(.system(size: 18, weight: .bold)).foregroundColor(.white)
                                Text(d.synopsis)
                                    .font(.system(size: 15)).foregroundColor(.gray).lineSpacing(6)
                            }
                            .padding(20)
                        }

                        // ── Episodes / Seasons  (selected season: white surface; play icon: white)
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
                                                            ? Color.white.opacity(0.22)
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
                                                        .foregroundColor(.white)
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
                videoUrl: data.videoUrl, videoUrl1080: data.videoUrl1080,
                videoUrl360: data.videoUrl360,
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
            videoUrl: d.movieUrl, videoUrl1080: d.movieUrl1080, videoUrl360: d.movieUrl360,
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

print("✅ UTan v4.0 – ALL ENHANCEMENTS APPLIED.")
print("   1. RED COLOR FULLY REMOVED – entire app now uses Dark Theme + Pure White accent.")
print("   2. HOME LAYOUT RE-ARCHITECTED:")
print("      – Hero section: full-screen immersive banner with bottom fade.")
print("      – History / Continue Watching: conditional (only when history exists).")
print("      – Network Navigation Cards: horizontal row — Netflix/Anime/Kids/Hbo/Disney/Marvel.")
print("      – Content Category Rows: dynamic scraped sections.")
print("      – Redundant duplicate section below Documentary row: REMOVED.")
print("   3. BRANDING: logo.png asset used in Home header and Video Player watermark.")
print("   4. project.pbxproj updated: Resources build phase added for all image assets.")
