import os, shutil

BASE  = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.path.join(BASE, "audio")
os.makedirs(AUDIO, exist_ok=True)

UP     = os.path.dirname(BASE)
FILES  = os.path.join(UP, "files")
WAVS   = os.path.join(UP, "study_wavs")
V1     = os.path.join(UP, "activity_levels_soni_v1")
V2     = os.path.join(UP, "activity_levels_soni_v2", "activity_stimuli_output")
SMOOTH = os.path.join(UP, "activity_levels_soni_v1", "smooth_pentatonic_outputs")

copies = [
    # Beethoven baseline + deformations
    (os.path.join(WAVS,  "baseline.wav"),        "beethoven_original.wav"),
    (os.path.join(WAVS,  "pitch_low.wav"),        "beethoven_pitch_low.wav"),
    (os.path.join(WAVS,  "pitch_mid.wav"),        "beethoven_pitch_mid.wav"),
    (os.path.join(WAVS,  "pitch_high.wav"),       "beethoven_pitch_high.wav"),
    (os.path.join(WAVS,  "rhythm_low.wav"),       "beethoven_rhythm_low.wav"),
    (os.path.join(WAVS,  "rhythm_mid.wav"),       "beethoven_rhythm_mid.wav"),
    (os.path.join(WAVS,  "rhythm_high.wav"),      "beethoven_rhythm_high.wav"),
    (os.path.join(WAVS,  "timbre_low.wav"),       "beethoven_timbre_low.wav"),
    (os.path.join(WAVS,  "timbre_mid.wav"),       "beethoven_timbre_mid.wav"),
    (os.path.join(WAVS,  "timbre_high.wav"),      "beethoven_timbre_high.wav"),
    (os.path.join(WAVS,  "combined_low.wav"),     "beethoven_combined_low.wav"),
    (os.path.join(WAVS,  "combined_mid.wav"),     "beethoven_combined_mid.wav"),
    (os.path.join(WAVS,  "combined_high.wav"),    "beethoven_combined_high.wav"),

    # Generative v2 — three intensity levels (major/minor/chromatic)
    (os.path.join(V2, "01_Low_all_day.wav"),      "gen_low.wav"),
    (os.path.join(V2, "02_Mid_all_day.wav"),      "gen_mid.wav"),
    (os.path.join(V2, "03_High_all_day.wav"),     "gen_high.wav"),

    # Generative v2 — pattern examples
    (os.path.join(V2, "05_Low-High-Low-High.wav"),         "gen_pattern_lohi.wav"),
    (os.path.join(V2, "07_Low-Mid-High-Low-Mid-High.wav"), "gen_pattern_ascending.wav"),
    (os.path.join(V2, "11_High-Mid-Low-High-Mid-Low.wav"), "gen_pattern_descending.wav"),

    # Smooth pentatonic outputs (v1)
    (os.path.join(SMOOTH, "01_smooth_Low_all_day.wav"),  "gen_smooth_low.wav"),
    (os.path.join(SMOOTH, "03_smooth_High_all_day.wav"), "gen_smooth_high.wav"),
]

print("Copying audio files...")
ok, fail = 0, 0
for src, name in copies:
    dst = os.path.join(AUDIO, name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        size = os.path.getsize(dst) // 1024
        print(f"  v  {name}  ({size} KB)")
        ok += 1
    else:
        print(f"  x  not found: {os.path.basename(src)}")
        fail += 1

# Copy video (large — may take a moment)
print("\nCopying video...")
vid_src = os.path.join(UP, "sonification_2022-08-09.mp4")
vid_dst = os.path.join(AUDIO, "fullday_video.mp4")
if os.path.exists(vid_src):
    shutil.copy2(vid_src, vid_dst)
    size = os.path.getsize(vid_dst) // (1024*1024)
    print(f"  v  fullday_video.mp4  ({size} MB)")
else:
    print(f"  x  video not found: {vid_src}")

print(f"\nDone: {ok} files copied, {fail} not found.")
print("Open website/index.html in your browser.")
