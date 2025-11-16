// Insecure: Detailed system error information exposed to the user
try {
    connectToDatabase();
} catch (SQLException e) {
    out.println("Database connection failed: " + e.getMessage());
}
