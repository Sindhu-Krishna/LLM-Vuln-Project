function deleteResourceSecure($id, $session_user_id) {
    // 1. Authentication check
    if (!isset($_SESSION['user_id']) || $_SESSION['user_id'] !== $session_user_id) {
        return "Error: Not authenticated.";
    }

    // 2. Authorization check (PROPERLY IMPLEMENTED) - Limits the action
    //    to resources that *also* match the current user's ID.
    $query = "DELETE FROM resources WHERE id = ? AND owner_user_id = ?";
    $result = $db->execute($query, [$id, $session_user_id]);

    if ($db->rowCount() === 0) {
        // This likely means the resource ID was invalid OR the resource
        // does not belong to the current user (Authorization Failure).
        return "Error: Resource not found or access denied (SECURE).";
    }

    return "Resource $id deleted successfully (SECURE).";
}
