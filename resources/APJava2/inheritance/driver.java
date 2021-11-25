public class driver {
    
    public static void main(String[] args)
    {
        Dog dog = new Dog("Snoopy", 10, 5);
        Animal bird = new Bird("Woodstock", 5, 100);
        Animal dolph = new Dolphin("Johnny", 7, 500);

        dog.normalSpeak();
        bird.magicSpeak();
        dolph.magicSpeak();
    }
}
