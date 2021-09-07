package classesPt1;

import java.util.ArrayList;

public class driver {

    public static void changeDogAge(Dog dog, int age)
    {
        System.out.println(dog);
        dog.setAge(age);
    }
    
    public static void main(String args[])
    {
        ArrayList<Integer> intList = new ArrayList<Integer>();
        intList.add(1);
        intList.add(2);
        intList.add(3);
        System.out.println(intList);

        ArrayList<String> strList = new ArrayList<String>();
        strList.add("Haha");
        strList.add("Yes");
        System.out.println(strList);

        Dog dog1 = new Dog("Sparky", "Yorkshire", 5);
        Dog dog2 = new Dog("Jonathan");
        Dog dog3 = new Dog();

        Dog refDog = dog1;

        System.out.println(refDog);
        System.out.println(dog1);
        System.out.println(dog2);

        changeDogAge(dog1, 7);
        System.out.println(dog1.getAge());

        dog1.setName("NotSparky");
        System.out.println(dog1.getName());

        ArrayList<Dog> dogList = new ArrayList<Dog>();
        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);

        // for (int i = 0; i < dogList.size(); i++)
        // {
        //     Dog tempDog = dogList.get(i);
        //     tempDog.sayHello();
        // }

        // For each loop in Java
        for (Dog tempDog : dogList)
            tempDog.sayHello();
        
        System.out.println("Total dogs: " + dog1.getDogsCreated());
    }
}