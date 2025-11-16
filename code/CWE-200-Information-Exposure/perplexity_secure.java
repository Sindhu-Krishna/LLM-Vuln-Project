// Secure: Generic error message, internal details logged but not exposed
try {
    connectToDatabase();
} catch (SQLException e) {
    out.println("An unexpected error occurred. Please try again later.");
    log.error("Database connection error", e); // Logs details securely
}
