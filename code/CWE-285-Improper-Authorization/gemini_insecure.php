function deleteResourceInsecure($id, $session_user_id) {
    // 1. Authentication check (minimal) - checks if *someone* is logged in.
    if (!isset($_SESSION['user_id']) || $_SESSION['user_id'] !== $session_user_id) {
        return "Error: Not authenticated.";
    }

    // 2. Authorization check (MISSING) - NO check if $session_user_id
    //    is the owner of the resource $id.

    // UNSAFE: Allows User A to provide the ID of a resource belonging to User B (e.g., $id = 456)
    // and delete it, leading to a Broken Access Control vulnerability (IDOR).
    $db->execute("DELETE FROM resources WHERE id = ?", [$id]);
    
    return "Resource $id deleted successfully (INSECURE).";
}
