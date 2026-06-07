import os

# Create directory structure
os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# 1. Write project.pbxproj
pbxproj_content = """// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 56;
	objects = {

/* Begin PBXBuildFile section */
		010101012C12345600000001 /* UTanApp.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000002 /* UTanApp.swift */; };
		010101012C12345600000003 /* Scraper.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000004 /* Scraper.swift */; };
		010101012C12345600000005 /* CustomPlayer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000006 /* CustomPlayer.swift */; };
		010101012C12345600000007 /* SubtitleParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000008 /* SubtitleParser.swift */; };
		010101012C12345600000009 /* Views.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000000A /* Views.swift */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		010101012C12345600000002 /* UTanApp.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = UTanApp.swift; sourceTree = "<group>"; };
		010101012C12345600000004 /* Scraper.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Scraper.swift; sourceTree = "<group>"; };
		010101012C12345600000006 /* CustomPlayer.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = CustomPlayer.swift; sourceTree = "<group>"; };
		010101012C12345600000008 /* SubtitleParser.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = SubtitleParser.swift; sourceTree = "<group>"; };
		010101012C1234560000000A /* Views.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Views.swift; sourceTree = "<group>"; };
		010101012C1234560000000B /* Info.plist */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
		010101012C1234560000000C /* UTan.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = UTan.app; sourceTree = BUILT_PRODUCTS_DIR; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		010101012C1234560000000D /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		010101012C1234560000000E /* MainGroup */ = {
			isa = PBXGroup;
			children = (
				010101012C1234560000000F /* UTan */,
				010101012C1234560000000C /* UTan.app */,
			);
			sourceTree = "<group>";
		};
		010101012C1234560000000F /* UTan */ = {
			isa = PBXGroup;
			children = (
				010101012C12345600000002 /* UTanApp.swift */,
				010101012C12345600000004 /* Scraper.swift */,
				010101012C12345600000006 /* CustomPlayer.swift */,
				010101012C12345600000008 /* SubtitleParser.swift */,
				010101012C1234560000000A /* Views.swift */,
				010101012C1234560000000B /* Info.plist */,
			);
			path = UTan;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		010101012C12345600000010 /* UTan */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 010101012C12345600000011 /* Build configuration list for PBXNativeTarget "UTan" */;
			buildPhases = (
				010101012C12345600000012 /* Sources */,
				010101012C1234560000000D /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = UTan;
			productName = UTan;
			productReference = 010101012C1234560000000C /* UTan.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		010101012C12345600000013 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				LastSwiftUpdateCheck = 1500;
				LastUpgradeCheck = 1500;
				TargetAttributes = {
					010101012C12345600000010 = {
						CreatedOnToolsVersion = 15.0;
						DevelopmentTeam = "";
					};
				};
			};
			buildConfigurationList = 010101012C12345600000014 /* Build configuration list for PBXProject "UTan" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = 010101012C1234560000000E /* MainGroup */;
			productRefGroup = 010101012C1234560000000E /* MainGroup */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				010101012C12345600000010 /* UTan */,
			);
		};
/* End PBXProject section */

/* Begin PBXSourcesBuildPhase section */
		010101012C12345600000012 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				010101012C12345600000001 /* UTanApp.swift in Sources */,
				010101012C12345600000003 /* Scraper.swift in Sources */,
				010101012C12345600000005 /* CustomPlayer.swift in Sources */,
				010101012C12345600000007 /* SubtitleParser.swift in Sources */,
				010101012C12345600000009 /* Views.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		010101012C12345600000015 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_AUDIT_TEXT_INCLUSION_IN_SHMEM_DISABLE = YES;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			};
			name = Debug;
		};
		010101012C12345600000016 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_AUDIT_TEXT_INCLUSION_IN_SHMEM_DISABLE = YES;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				MTL_FAST_MATH = YES;
				SDKROOT = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		010101012C12345600000017 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Manual;
				CODE_SIGNING_ALLOWED = NO;
				CODE_SIGNING_REQUIRED = NO;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "";
				ENABLE_PREVIEWS = YES;
				INFOPLIST_FILE = UTan/Info.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 15.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		010101012C12345600000018 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Manual;
				CODE_SIGNING_ALLOWED = NO;
				CODE_SIGNING_REQUIRED = NO;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "";
				ENABLE_PREVIEWS = YES;
				INFOPLIST_FILE = UTan/Info.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 15.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		010101012C12345600000011 /* Build configuration list for PBXNativeTarget "UTan" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				010101012C12345600000017 /* Debug */,
				010101012C12345600000018 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		010101012C12345600000014 /* Build configuration list for PBXProject "UTan" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				010101012C12345600000015 /* Debug */,
				010101012C12345600000016 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 010101012C12345600000013 /* Project object */;
}
"""

with open("UTan/UTan.xcodeproj/project.pbxproj", "w", encoding="utf-8") as f:
    f.write(pbxproj_content)

# 2. Write Info.plist
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
	<string>1.0</string>
	<key>CFBundleVersion</key>
	<string>1</string>
	<key>LSRequiresIPhoneOS</key>
	<true/>
	<key>NSAppTransportSecurity</key>
	<dict>
		<key>NSAllowsArbitraryLoads</key>
		<true/>
	</dict>
	<key>UILaunchScreen</key>
	<dict/>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
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
            ContentView()
        }
    }
}
"""

with open("UTan/UTan/UTanApp.swift", "w", encoding="utf-8") as f:
    f.write(app_swift)

# 4. Read and Write Swift files from current directory
# These files were moved to the root of the repo
swift_files = ["Scraper.swift", "CustomPlayer.swift", "Views.swift", "SubtitleParser.swift"]

for file_name in swift_files:
    # Read from current directory (where generate_project.py is)
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
        # Write to the project directory structure
        dst_path = os.path.join("UTan/UTan", file_name)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Project UTan PREMIUM setup successfully generated using external Swift assets.")
