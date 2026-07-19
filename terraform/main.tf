resource "kubernetes_namespace_v1" "homework" {
    metadata {
        name = var.namespace
    }
}

resource "helm_release" "myapp" {
    name       = "myapp"
    repository = var.chart_repo
    chart      = "myapp"
    version    = var.chart_version
    namespace  = kubernetes_namespace_v1.homework.metadata[0].name

    set = [{
        name  = "image.tag"
        value = var.image_tag
    },
    {
        name  = "image.repository"
        value = var.image_repo
    },
    {
        name  = "environment"
        value = var.environment
    }]
}