<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
            <router-link :to="{ name: 'home' }" class="navbar-brand">
                QuestionTime
            </router-link> 

        <!-- <a class="navbar-brand" href="#">Navbar</a> -->
      
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto">
            <li class="nav-item mx-1">
                <button class="btn btn-outline-secondary" href="/accounts/logout/">Logout</button>
            </li>
        </ul>
      </div>
    </div>
    </nav>
</template>

<script>
export default {
    name: "NavbarComponent",
};
</script>

<style>
.my-navbar {
    border-bottom: 1px solid #ddd;
}

.navbar-brand {
    font-weight: bold;
    font-size: 150%;
}

.navbar-brand:hover {
    color: #dc3545 !important;
}
</style>