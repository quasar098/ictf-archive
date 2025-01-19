import java.util.Random;

public class SlightlyMoreSecureRandom {
    //Implementation of a version of Xoroshiro128
    private long seedLo;
    private long seedHi;
    public SlightlyMoreSecureRandom(){
        this(new Random().nextLong(), new Random().nextLong());
    }
    public SlightlyMoreSecureRandom(long l, long l2) {
        this.seedLo = l;
        this.seedHi = l2;
        if ((this.seedLo | this.seedHi) == 0L) {
            this.seedLo = -7046029254386353131L;
            this.seedHi = 7640891576956012809L;
        }
    }

    public long nextLong() {
        long l = this.seedLo;
        long l2 = this.seedHi;
        long l3 = Long.rotateLeft(l + l2, 17) + l;
        this.seedLo = Long.rotateLeft(l, 49) ^ (l2 ^= l) ^ l2 << 21;
        this.seedHi = Long.rotateLeft(l2, 28);
        return l3;
    }

    public long next(){
        return nextLong();
    }
}
