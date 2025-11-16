// Insecure: No validation on user input
Scanner scanner = new Scanner(System.in);
System.out.print("Enter your age: ");
int age = scanner.nextInt();  // No checks; negative or excessively large values accepted.
System.out.println("Your age is: " + age);
