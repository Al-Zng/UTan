import SwiftUI
import AVKit

struct CustomPlayer: View {
    let url: URL
    @Environment(\.dismiss) var dismiss
    @State private var player = AVPlayer()
    @State private var showControls = true
    @State private var isDoubleSpeed = false
    @State private var progress: Double = 0
    @State private var duration: Double = 1
    
    var body: some View {
        ZStack {
            VideoPlayer(player: player)
                .onAppear {
                    player.replaceCurrentItem(with: AVPlayerItem(url: url))
                    player.play()
                }
            
            if showControls {
                ZStack {
                    Color.black.opacity(0.4).ignoresSafeArea()
                    
                    VStack {
                        HStack {
                            Button { dismiss() } label: {
                                Image(systemName: "chevron.left").font(.title2).foregroundColor(.white)
                            }
                            Spacer()
                        }.padding()
                        
                        Spacer()
                        
                        HStack(spacing: 40) {
                            Button { player.seek(to: player.currentTime() - CMTime(seconds: 10, preferredTimescale: 1)) } label: {
                                Image(systemName: "gobackward.10").font(.largeTitle)
                            }
                            Button { player.timeControlStatus == .playing ? player.pause() : player.play() } label: {
                                Image(systemName: player.timeControlStatus == .playing ? "pause.fill" : "play.fill").font(.system(size: 50))
                            }
                            Button { player.seek(to: player.currentTime() + CMTime(seconds: 10, preferredTimescale: 1)) } label: {
                                Image(systemName: "goforward.10").font(.largeTitle)
                            }
                        }.foregroundColor(.white)
                        
                        Spacer()
                    }
                }
            }
        }
        .onTapGesture { withAnimation { showControls.toggle() } }
        .gesture(LongPressGesture(minimumDuration: 0.5).onEnded { _ in
            isDoubleSpeed = true
            player.rate = 2.0
        })
        .simultaneousGesture(DragGesture(minimumDistance: 0).onEnded { _ in
            if isDoubleSpeed {
                isDoubleSpeed = false
                player.rate = 1.0
            }
        })
        .navigationBarHidden(true)
    }
}
