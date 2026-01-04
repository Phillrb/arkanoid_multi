import os
import os.path
import sys
import hashlib
from zipfile import ZipFile

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

def make_combined_file(SRC1, SRC2, DST, HASH, OUT, NAME):
    if os.path.exists(DST):
        os.remove(DST)
    out_file = open(DST, "ab")
    with open(SRC1, "rb") as file:
        byte_nxt = file.read(1)
        while byte_nxt != b"":
            out_file.write(byte_nxt)
            byte_nxt = file.read(1)
    with open(SRC2, "rb") as file:
        byte_nxt = file.read(1)
        while byte_nxt != b"":
            out_file.write(byte_nxt)
            byte_nxt = file.read(1)
    out_file.close()
    if not os.path.exists(DST): 
        sys.exit("ERROR: File not created at: " + DST)
    tmpHash = hash_file(DST)
    if tmpHash != HASH:
        sys.exit("ERROR: File hash '" + tmpHash  +"' does not match expected '" + HASH + "' at " + DST)
    if os.path.exists(OUT):
        os.remove(OUT)
    os.rename(DST, OUT)
    print(">>> " + NAME + " is at: " + OUT)

def check_exists(SRC, NAME):
    if not os.path.exists(SRC): 
        sys.exit("ERROR: " + NAME + " File not found at: " + SRC)
    print("- " + NAME + " File found")

def check_rom(SRC, HASH, NAME):
    check_exists(SRC, NAME)
    tmpHash = hash_file(SRC)
    if tmpHash != HASH:
        sys.exit("ERROR: " + NAME + " ROM hash '" + tmpHash + "' does not match expected '" + HASH + "'")
    print("- " + NAME + " ROM found and validated")


SCRIPT_DIR = os.path.dirname(__file__)
SRC_DIR =  os.path.abspath(os.path.join(SCRIPT_DIR, 'source'))
ARKANOID_ROM = os.path.join(SRC_DIR, "arkanoid.zip")
ARKATAYT_ROM = os.path.join(SRC_DIR, "arkatayt.zip")
ARKATOUR_ROM = os.path.join(SRC_DIR, "arkatour.zip")
TMP_DIR =  os.path.abspath(os.path.join(SCRIPT_DIR, 'tmp'))
ARKANOID_IC22 = os.path.join(TMP_DIR,"a75-09.ic22")
ARKANOID_IC23 = os.path.join(TMP_DIR,"a75-08.ic23")
ARKANOID_IC24 = os.path.join(TMP_DIR,"a75-07.ic24")
ARKATOUR_IC22 = os.path.join(TMP_DIR,"a75-35.ic22")
ARKATOUR_IC23 = os.path.join(TMP_DIR,"a75-34.ic23")
ARKATOUR_IC24 = os.path.join(TMP_DIR,"a75-33.ic24")
ARKANOID_IC62 = os.path.join(TMP_DIR,"a75__05.ic62")
ARKANOID_IC63 = os.path.join(TMP_DIR,"a75__04.ic63")
ARKANOID_IC64 = os.path.join(TMP_DIR,"a75__03.ic64")
ARKATOUR_IC62 = os.path.join(TMP_DIR,"a75__31.ic62")
ARKATOUR_IC63 = os.path.join(TMP_DIR,"a75__30.ic63")
ARKATOUR_IC64 = os.path.join(TMP_DIR,"a75__29.ic64")
MULTI_COLOR_PROM_NAME = "a75_multi_color_prom_27c160.bin"
MULTI_COLOR_PROM = os.path.join(TMP_DIR, MULTI_COLOR_PROM_NAME)
MULTI_COLOR_PROM_HASH = "ced954adbb489b1d1e3522af48252e7d6368bf87"
OUT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, 'output'))
DST_MULTI_COLOR_PROM = os.path.join(OUT_DIR, MULTI_COLOR_PROM_NAME)
IC62_COMBINED_NAME = "a75_multi.ic62"
IC63_COMBINED_NAME = "a75_multi.ic63"
IC64_COMBINED_NAME = "a75_multi.ic64"
IC62_COMBINED = os.path.join(TMP_DIR, IC62_COMBINED_NAME)
IC62_COMBINED_HASH = "e9f6978614f7ff543dd128e3eb1e9d00f0fed5b7"
IC63_COMBINED = os.path.join(TMP_DIR, IC63_COMBINED_NAME)
IC63_COMBINED_HASH = "a8bb6b9d6dffd5c7b2ba21e7a86befd36687151d"
IC64_COMBINED = os.path.join(TMP_DIR, IC64_COMBINED_NAME)
IC64_COMBINED_HASH = "f7dc5d9acbb05a20e4178ccc053735ea6c34d5dd"
DST_IC62_COMBINED = os.path.join(OUT_DIR, IC62_COMBINED_NAME)
DST_IC63_COMBINED = os.path.join(OUT_DIR, IC63_COMBINED_NAME)
DST_IC64_COMBINED = os.path.join(OUT_DIR, IC64_COMBINED_NAME)
ARKATAYT_IC81_PATCH = os.path.join(SRC_DIR, "ic81-v_patched.3f")
ARKATAYT_IC82_PATCH = os.path.join(SRC_DIR, "ic82-w_patched.5f")
ARKATAYT_IC81_PATCH_HASH = "1c10f9a15ff6ed2c25045edc900f4b5b71f63af8"
ARKATAYT_IC82_PATCH_HASH = "a52c9ab90b78dbd2658072ec7939cad45a657486"
ARKATOUR_IC16_PATCH = os.path.join(SRC_DIR, "a75__28_patched.ic16")
ARKATOUR_IC17_PATCH = os.path.join(SRC_DIR, "a75__27_patched.ic17")
ARKATOUR_IC16_PATCH_HASH = "6fdd0d4d4a56eadb942aeb2b55f45a359cf1ca93"
ARKATOUR_IC17_PATCH_HASH = "52062f168bcb29ec49993804b7628e6553c3f681"
IC82_16_PATCH_COMBINED_NAME = "a75_multi_patched.ic16"
IC81_17_PATCH_COMBINED_NAME = "a75_multi_patched.ic17"
IC82_16_PATCH_COMBINED = os.path.join(TMP_DIR, IC82_16_PATCH_COMBINED_NAME)
IC81_17_PATCH_COMBINED = os.path.join(TMP_DIR, IC81_17_PATCH_COMBINED_NAME)
IC82_16_PATCH_COMBINED_HASH = "b4fd6c42be68b7f8ef593546f5129967fcc1a029" 
IC81_17_PATCH_COMBINED_HASH = "332ca8181008080e08bc91bfde3aa13566120f93"
DST_IC82_16_PATCH_COMBINED = os.path.join(OUT_DIR, IC82_16_PATCH_COMBINED_NAME)
DST_IC81_17_PATCH_COMBINED = os.path.join(OUT_DIR, IC81_17_PATCH_COMBINED_NAME)

print ("Looking for original ROMs:")

check_exists(ARKANOID_ROM, "Original Arkanoid zip")
check_exists(ARKATAYT_ROM, "Boot Arkanoid 'arkatayt' zip")
check_exists(ARKATOUR_ROM, "Tournament Arkanoid zip")
check_rom(ARKATAYT_IC81_PATCH, ARKATAYT_IC81_PATCH_HASH, "Patched Arkatayt ic81")
check_rom(ARKATAYT_IC82_PATCH, ARKATAYT_IC82_PATCH_HASH, "Patched Arkatayt ic82")
check_rom(ARKATOUR_IC16_PATCH, ARKATOUR_IC16_PATCH_HASH, "Patched Tournament ic16")
check_rom(ARKATOUR_IC17_PATCH, ARKATOUR_IC17_PATCH_HASH, "Patched Tournament ic17")


print("Creating combined color PROM file for 27c160:")

# Create temp dir
if not os.path.exists(TMP_DIR): 
    os.mkdir(TMP_DIR)

# unzip to temp dir
with ZipFile(ARKANOID_ROM, 'r') as zObject:
    zObject.extractall(TMP_DIR)
with ZipFile(ARKATOUR_ROM, 'r') as zObject:
    zObject.extractall(TMP_DIR)

# combine contents
if os.path.exists(MULTI_COLOR_PROM):
    os.remove(MULTI_COLOR_PROM)
out_file = open(MULTI_COLOR_PROM, "ab")
for x in range(0, 1024):
    with open(ARKANOID_IC22, "rb") as pB:
        with open(ARKANOID_IC23, "rb") as pG:
            with open(ARKANOID_IC24, "rb") as pR:
                byte_promB = pB.read(1)
                byte_promG = pG.read(1)
                byte_promR = pR.read(1)

                while byte_promB != b"" and byte_promG != b"" and byte_promR != b"":
                    out_file.write(((int.from_bytes(byte_promG, byteorder='big') << 4) + int.from_bytes(byte_promB, byteorder='big')).to_bytes(1, byteorder='big'))
                    out_file.write(byte_promR)

                    # Next bytes
                    byte_promB = pB.read(1)
                    byte_promG = pG.read(1)
                    byte_promR = pR.read(1)

    with open(ARKATOUR_IC22, "rb") as pB:
        with open(ARKATOUR_IC23, "rb") as pG:
            with open(ARKATOUR_IC24, "rb") as pR:
                byte_promB = pB.read(1)
                byte_promG = pG.read(1)
                byte_promR = pR.read(1)

                while byte_promB != b"" and byte_promG != b"" and byte_promR != b"":
                    out_file.write(((int.from_bytes(byte_promG, byteorder='big') << 4) + int.from_bytes(byte_promB, byteorder='big')).to_bytes(1, byteorder='big'))
                    out_file.write(byte_promR)

                    # Next bytes
                    byte_promB = pB.read(1)
                    byte_promG = pG.read(1)
                    byte_promR = pR.read(1)

out_file.close()

# check hash
if not os.path.exists(MULTI_COLOR_PROM): 
    sys.exit("ERROR: MULTI_COLOR_PROM not found at: " + MULTI_COLOR_PROM)
tmpHash = hash_file(MULTI_COLOR_PROM)
if tmpHash != MULTI_COLOR_PROM_HASH:
    sys.exit("ERROR: MULTI_COLOR_PROM hash '" + tmpHash  +"' does not match expected '" + MULTI_COLOR_PROM_HASH + "'")

# move to output
if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)
if os.path.exists(DST_MULTI_COLOR_PROM):
    os.remove(DST_MULTI_COLOR_PROM)
os.rename(MULTI_COLOR_PROM, DST_MULTI_COLOR_PROM)
print(">>> " + MULTI_COLOR_PROM_NAME + " ROM for 27c160 is at: " + DST_MULTI_COLOR_PROM)

print("Combining other ROMs")
make_combined_file(ARKANOID_IC62, ARKATOUR_IC62, IC62_COMBINED, IC62_COMBINED_HASH, DST_IC62_COMBINED, IC62_COMBINED_NAME + " ROM for 27c512")
make_combined_file(ARKANOID_IC63, ARKATOUR_IC63, IC63_COMBINED, IC63_COMBINED_HASH, DST_IC63_COMBINED, IC63_COMBINED_NAME + " ROM for 27c512")
make_combined_file(ARKANOID_IC64, ARKATOUR_IC64, IC64_COMBINED, IC64_COMBINED_HASH, DST_IC64_COMBINED, IC64_COMBINED_NAME + " ROM for 27c512")

print("Combining patched program ROMs to bypass MCU and add Freeplay etc")
make_combined_file(ARKATAYT_IC82_PATCH, ARKATOUR_IC16_PATCH, IC82_16_PATCH_COMBINED, IC82_16_PATCH_COMBINED_HASH, DST_IC82_16_PATCH_COMBINED, IC82_16_PATCH_COMBINED_NAME + " ROM for 27c512")
make_combined_file(ARKATAYT_IC81_PATCH, ARKATOUR_IC17_PATCH, IC81_17_PATCH_COMBINED, IC81_17_PATCH_COMBINED_HASH, DST_IC81_17_PATCH_COMBINED, IC81_17_PATCH_COMBINED_NAME + " ROM for 27c512")

print("Clean up")
for root, dirs, files in os.walk(TMP_DIR):
    for file in files:
        os.remove(os.path.join(root, file))
if os.path.exists(TMP_DIR):
    os.removedirs(TMP_DIR)
