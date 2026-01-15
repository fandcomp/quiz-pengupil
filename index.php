# index.php - Landing Page untuk Testing

<?php
session_start();

// Redirect jika belum login
if(!isset($_SESSION['username'])) {
    header('Location: login.php');
    exit();
}

$username = $_SESSION['username'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Quiz Pengupil</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header bg-primary text-white">
                        <h4>Welcome to Dashboard</h4>
                    </div>
                    <div class="card-body">
                        <h5>Hello, <span id="username-display"><?= htmlspecialchars($username); ?></span>!</h5>
                        <p class="text-success" id="login-success-message">Anda berhasil login ke sistem.</p>
                        <hr>
                        <p>Ini adalah halaman dashboard untuk testing aplikasi Quiz Pengupil.</p>
                        <div class="mt-4">
                            <a href="logout.php" class="btn btn-danger" id="logout-button">Logout</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
</body>
</html>
