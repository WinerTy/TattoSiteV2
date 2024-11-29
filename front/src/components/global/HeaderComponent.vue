<script setup lang="ts">
import { RouterLink } from 'vue-router'
import SalonSelectro from '../shared/SalonSelector.vue';
import { RoutePath } from '@/types/router.type'

const links = [
    {
        title: 'О салоне',
        link: RoutePath.AboutSalon
    },
    {
        title: 'Мастера',
        link: RoutePath.Masters
    },
    {
        title: "О нас",
        link: RoutePath.About
    },
    {
        title: "Контакты",
        link: RoutePath.Contacts
    },
]
</script>

<template>
    <header class="my-header">
        <div class="logo">
            <RouterLink to="/"><h1>Logo</h1></RouterLink>
        </div>
        <nav class="links ">
            <SalonSelectro />
            <RouterLink v-for="link in links" :key="link.title" :to="link.link" class="des-l nav-link nav-size p-5-10">
                {{ link.title }}
            </RouterLink>
        </nav>
    </header>
</template>


<style scoped>
    .my-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px;
        position: fixed;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        background-color: var(--secondary);
        color: var(--white);
        z-index: 2;
        max-width: 1440px;
        width: 100%;
    }
    .links {
        display: flex;
        gap: 50px;        
    }
    .nav-link {
        color: var(--white);
        text-decoration: none;
        width: fit-content;
    }
    .nav-link:hover {
        text-decoration: underline;
    }
    .logo h1{
        color: var(--quinary) !important; 
    }
</style>