// Secure: With input validation
Scanner scanner = new Scanner(System.in);
System.out.print("Enter your age: ");
if (scanner.hasNextInt()) {
    int age = scanner.nextInt();
    if (age >= 0 && age <= 120) {  // Checks limits to reasonable values
        System.out.println("Your age is: " + age);
    } else {
        System.out.println("Invalid age. Please enter a value between 0 and 120.");
    }
} else {
    System.out.println("Invalid input. Please enter a numerical value.");
}
