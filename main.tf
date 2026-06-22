terraform {
    required_providers {
        docker = {
            source = "kreuzwerker/docker"
            version = "~> 3.0.0"
        }
    }
}

provider"docker" {}

# Membuat kontainer Ubuntu kosong sebagai simulasi server
resource "docker_container" "server_data" {
    name  = "server_uas_analitik"
    image = "ubuntu:latest"

    # Membuat kontainer tetap hidup di latar belakang
    command = ["tail", "-f", "/dev/null"]
}