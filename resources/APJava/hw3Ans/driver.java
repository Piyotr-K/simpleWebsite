package src.hw3;

public class driver {
    
    public static void main(String[] args)
    {
        Cat c1 = new Cat("Garfielf", 43, 70.0);
        Dolphin d1 = new Dolphin("Flipper", 30, 500);
        Bird b1 = new Bird("Twocans", 12, 200);

        c1.speak();
        d1.speak(b1);
        b1.speak(c1);
    }
}
