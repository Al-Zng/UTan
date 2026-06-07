import SwiftUI
import AVKit

enum VideoQuality: String, CaseIterable, Identifiable {
    case auto = "Auto"
    case p1080 = "1080p"
    case p360 = "360p"
    
    var id: String { self.rawValue }
}

enum VideoFitMode: String, CaseIterable, Identifiable {
    case fit = "Fit (MX)"
    case fill = "Stretch Fill"
    case zoom = "16:9 Crop"
    
    var id: String { self.rawValue }
    
    var gravity: AVLayerVideoGravity {
        switch self {
        case .fit: return .resizeAspect
        case .fill: return .resize
        case .zoom: return .resizeAspectFill
        }
    }
}

struct VideoPlayerRepresentable: UIViewControllerRepresentable {
    let player: AVPlayer
    let gravity: AVLayerVideoGravity
    
    func makeUIViewController(context: Context) -> AVPlayerViewController {
        let controller = AVPlayerViewController()
        controller.player = player
        controller.showsPlaybackControls = false
        controller.videoGravity = gravity
        return controller
    }
    
    func updateUIViewController(_ uiViewController: AVPlayerViewController, context: Context) {
        uiViewController.videoGravity = gravity
    }
}

struct CustomPlayerView: View {
    let videoUrl: String
    let videoUrl1080: String
    let videoUrl360: String
    let subtitleUrl: String
    let webvttUrl: String
    
    @Environment(\.presentationMode) var presentationMode
    @State private var player: AVPlayer?
    @State private var isPlaying = true
    @State private var currentTime: TimeInterval = 0
    @State private var duration: TimeInterval = 0
    @State private var cues: [SubtitleCue] = []
    @State private var activeSubtitleText = ""
    @State private var isSpeedUpActive = false
    @State private var isLocked = false
    @State private var fitMode: VideoFitMode = .fit
    @State private var playbackSpeed: Double = 1.0
    @State private var showSettings = false
    @State private var showControls = true
    @State private var selectedQuality: VideoQuality = .auto
    
    @State private var fontSize: CGFloat = 22
    @State private var verticalOffset: CGFloat = 50
    @State private var timeObserver: Any?
    @State private var controlsTimer: Timer?
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            if let player = player {
                VideoPlayerRepresentable(player: player, gravity: fitMode.gravity)
                    .ignoresSafeArea()
                    .onTapGesture {
                        withAnimation {
                            showControls.toggle()
                        }
                        if showControls {
                            resetControlsTimer()
                        }
                    }
                    .gesture(
                        LongPressGesture(minimumDuration: 0.5)
                            .onChanged { _ in
                                if !isLocked {
                                    self.isSpeedUpActive = true
                                    player.rate = Float(2.0)
                                }
                            }
                            .onEnded { _ in
                                if !isLocked {
                                    self.isSpeedUpActive = false
                                    player.rate = Float(self.isPlaying ? playbackSpeed : 0.0)
                                }
                            }
                    )
                
                if !activeSubtitleText.isEmpty {
                    VStack {
                        Spacer()
                        Text(activeSubtitleText)
                            .font(.system(size: fontSize, weight: .bold, design: .rounded))
                            .foregroundColor(.yellow)
                            .shadow(color: .black, radius: 5, x: 2, y: 2)
                            .padding(.horizontal, 16)
                            .padding(.vertical, 8)
                            .background(Color.black.opacity(0.65))
                            .cornerRadius(10)
                            .multilineTextAlignment(.center)
                            .padding(.bottom, verticalOffset)
                    }
                    .padding(.horizontal, 30)
                    .allowsHitTesting(false)
                }
                
                if isSpeedUpActive {
                    VStack {
                        HStack(spacing: 6) {
                            Image(systemName: "forward.frame.fill")
                            Text("2.0X Fast Forward")
                                .font(.system(size: 14, weight: .bold))
                        }
                        .font(.caption)
                        .foregroundColor(.white)
                        .padding(.horizontal, 16)
                        .padding(.vertical, 8)
                        .background(Color(red: 0.89, green: 0.04, blue: 0.08).opacity(0.85))
                        .cornerRadius(20)
                        .padding(.top, 30)
                        Spacer()
                    }
                }
                
                if showControls || isLocked {
                    VStack {
                        // Top Bar
                        HStack {
                            if !isLocked {
                                Button(action: {
                                    shutdownPlayer()
                                    presentationMode.wrappedValue.dismiss()
                                }) {
                                    Image(systemName: "arrow.backward")
                                        .font(.title2)
                                        .foregroundColor(.white)
                                        .padding(12)
                                        .background(Color.black.opacity(0.5))
                                        .clipShape(Circle())
                                }
                            }
                            
                            Spacer()
                            
                            Button(action: { 
                                isLocked.toggle()
                                if isLocked { showControls = false }
                                else { showControls = true; resetControlsTimer() }
                            }) {
                                Image(systemName: isLocked ? "lock.fill" : "lock.open.fill")
                                    .font(.title2)
                                    .foregroundColor(isLocked ? .red : .white)
                                    .padding(12)
                                    .background(Color.black.opacity(0.5))
                                    .clipShape(Circle())
                            }
                            
                            if !isLocked {
                                Menu {
                                    Picker("Quality", selection: $selectedQuality) {
                                        Text("Auto").tag(VideoQuality.auto)
                                        if !videoUrl1080.isEmpty { Text("1080p").tag(VideoQuality.p1080) }
                                        if !videoUrl360.isEmpty { Text("360p").tag(VideoQuality.p360) }
                                    }
                                } label: {
                                    Image(systemName: "highquality")
                                        .font(.title2)
                                        .foregroundColor(.white)
                                        .padding(12)
                                        .background(Color.black.opacity(0.5))
                                        .clipShape(Circle())
                                }
                                .onChange(of: selectedQuality) { _ in
                                    switchQuality()
                                }

                                Button(action: {
                                    if fitMode == .fit { fitMode = .fill }
                                    else if fitMode == .fill { fitMode = .zoom }
                                    else { fitMode = .fit }
                                    resetControlsTimer()
                                }) {
                                    Image(systemName: "aspectratio.fill")
                                        .font(.title2)
                                        .foregroundColor(.white)
                                        .padding(12)
                                        .background(Color.black.opacity(0.5))
                                        .clipShape(Circle())
                                }
                                
                                Button(action: { showSettings.toggle(); resetControlsTimer() }) {
                                    Image(systemName: "gearshape.fill")
                                        .font(.title2)
                                        .foregroundColor(.white)
                                        .padding(12)
                                        .background(Color.black.opacity(0.5))
                                        .clipShape(Circle())
                                }
                            }
                        }
                        .padding(.horizontal)
                        .padding(.top, 20)
                        .opacity(isLocked && !showControls ? 0.3 : 1.0)
                        
                        Spacer()
                        
                        // Bottom Controls
                        if !isLocked && showControls {
                            VStack(spacing: 15) {
                                HStack {
                                    Text(formatTime(currentTime))
                                        .font(.caption)
                                        .monospacedDigit()
                                        .foregroundColor(.white)
                                    
                                    Slider(value: $currentTime, in: 0...max(duration, 1), onEditingChanged: { editing in
                                        if !editing {
                                            player.seek(to: CMTime(seconds: currentTime, preferredTimescale: 600))
                                            resetControlsTimer()
                                        } else {
                                            controlsTimer?.invalidate()
                                        }
                                    })
                                    .accentColor(Color(red: 0.89, green: 0.04, blue: 0.08))
                                    
                                    Text(formatTime(duration))
                                        .font(.caption)
                                        .monospacedDigit()
                                        .foregroundColor(.white)
                                }
                                .padding(.horizontal)
                                
                                HStack(spacing: 50) {
                                    Button(action: {
                                        player.seek(to: CMTime(seconds: max(0, currentTime - 10), preferredTimescale: 600))
                                        resetControlsTimer()
                                    }) {
                                        Image(systemName: "gobackward.10")
                                            .font(.title)
                                            .foregroundColor(.white)
                                    }
                                    
                                    Button(action: {
                                        if isPlaying {
                                            player.pause()
                                        } else {
                                            player.play()
                                            player.rate = Float(playbackSpeed)
                                        }
                                        isPlaying.toggle()
                                        resetControlsTimer()
                                    }) {
                                        Image(systemName: isPlaying ? "pause.circle.fill" : "play.circle.fill")
                                            .font(.system(size: 60))
                                            .foregroundColor(.white)
                                    }
                                    
                                    Button(action: {
                                        player.seek(to: CMTime(seconds: min(duration, currentTime + 10), preferredTimescale: 600))
                                        resetControlsTimer()
                                    }) {
                                        Image(systemName: "goforward.10")
                                            .font(.title)
                                            .foregroundColor(.white)
                                    }
                                }
                                .padding(.bottom, 25)
                            }
                            .background(
                                LinearGradient(colors: [.clear, .black.opacity(0.85)], startPoint: .top, endPoint: .bottom)
                            )
                        }
                    }
                }
            }
        }
        .statusBar(hidden: true)
        .onAppear {
            setupPlayer()
            resetControlsTimer()
        }
        .onDisappear {
            shutdownPlayer()
            controlsTimer?.invalidate()
        }
        .sheet(isPresented: $showSettings) {
            MXSettingsView(fontSize: $fontSize, verticalOffset: $verticalOffset, playbackSpeed: $playbackSpeed, player: player)
        }
    }
    
    private func resetControlsTimer() {
        controlsTimer?.invalidate()
        controlsTimer = Timer.scheduledTimer(withTimeInterval: 5.0, repeats: false) { _ in
            withAnimation {
                showControls = false
            }
        }
    }
    
    private func setupPlayer() {
        let currentPos = currentTime
        let urlString: String
        switch selectedQuality {
        case .auto: urlString = videoUrl
        case .p1080: urlString = videoUrl1080.isEmpty ? videoUrl : videoUrl1080
        case .p360: urlString = videoUrl360.isEmpty ? videoUrl : videoUrl360
        }
        
        guard let url = URL(string: urlString) else { return }
        let playerItem = AVPlayerItem(url: url)
        let newPlayer = AVPlayer(playerItem: playerItem)
        self.player = newPlayer
        
        if currentPos > 0 {
            newPlayer.seek(to: CMTime(seconds: currentPos, preferredTimescale: 600))
        }
        
        if isPlaying {
            newPlayer.play()
            newPlayer.rate = Float(playbackSpeed)
        }
        
        NotificationCenter.default.addObserver(forName: .AVPlayerItemDidPlayToEndTime, object: playerItem, queue: .main) { _ in
            self.isPlaying = false
            self.showControls = true
        }
        
        Task {
            if let dur = try? await playerItem.asset.load(.duration) {
                DispatchQueue.main.async {
                    self.duration = dur.seconds
                }
            }
        }
        
        self.timeObserver = newPlayer.addPeriodicTimeObserver(forInterval: CMTime(seconds: 0.2, preferredTimescale: 600), queue: .main) { time in
            self.currentTime = time.seconds
            if let activeCue = cues.first(where: { time.seconds >= $0.startTime && time.seconds <= $0.endTime }) {
                self.activeSubtitleText = activeCue.text
            } else {
                self.activeSubtitleText = ""
            }
        }
        
        // Try VTT first, then SRT
        let subUrl = webvttUrl.isEmpty ? subtitleUrl : webvttUrl
        if !subUrl.isEmpty {
            SubtitleParser.parse(url: subUrl) { parsedCues in
                self.cues = parsedCues
            }
        }
    }
    
    private func switchQuality() {
        let currentPos = currentTime
        shutdownPlayer()
        currentTime = currentPos
        setupPlayer()
    }
    
    private func shutdownPlayer() {
        if let observer = timeObserver {
            player?.removeTimeObserver(observer)
            timeObserver = nil
        }
        player?.pause()
        player = nil
    }
    
    private func formatTime(_ seconds: TimeInterval) -> String {
        let hrs = Int(seconds) / 3600
        let mins = (Int(seconds) % 3600) / 60
        let secs = Int(seconds) % 60
        if hrs > 0 {
            return String(format: "%02d:%02d:%02d", hrs, mins, secs)
        }
        return String(format: "%02d:%02d", mins, secs)
    }
}

struct MXSettingsView: View {
    @Binding var fontSize: CGFloat
    @Binding var verticalOffset: CGFloat
    @Binding var playbackSpeed: Double
    var player: AVPlayer?
    
    @Environment(\.presentationMode) var presentationMode
    let speeds = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
    
    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("MX Audio Speed / سرعة الفيديو")) {
                    Picker("Speed Factor", selection: $playbackSpeed) {
                        ForEach(speeds, id: \.self) { speed in
                            Text(String(format: "%.2fx", speed)).tag(speed)
                        }
                    }
                    .pickerStyle(SegmentedPickerStyle())
                    .onChange(of: playbackSpeed) { newValue in
                        player?.rate = Float(newValue)
                    }
                }
                
                Section(header: Text("Subtitle Sizing / حجم الترجمة")) {
                    Slider(value: $fontSize, in: 16...36, step: 1)
                    Text("Font Size: \(Int(fontSize)) pt").font(.caption).foregroundColor(.gray)
                }
                
                Section(header: Text("Vertical Padding / الارتفاع من الأسفل")) {
                    Slider(value: $verticalOffset, in: 20...160, step: 5)
                    Text("Y-Offset: \(Int(verticalOffset)) px").font(.caption).foregroundColor(.gray)
                }
            }
            .navigationTitle("MX Engine Settings")
            .navigationBarItems(trailing: Button("Apply") {
                presentationMode.wrappedValue.dismiss()
            })
        }
    }
}
