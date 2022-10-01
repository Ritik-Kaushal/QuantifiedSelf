<template>
    <div>
        <div class="alert alert-success my-2 mx-3 " role = "alert">
            <h4>Welcome</h4>
            <hr>
            <p><strong>Gabrielle Hamilton</strong>, a chef in New York City, during an interview with the New York Times, said, "The one thing I see that consistently separates the chef from the home cook is that we taste everything, all the time, before we commit it to the dish, right down to the grains of salt. We slurp shot glasses of olive oil and acrate them in our mouths as if it were a wine we were trying to know. We taste the lamb, the fish, the butter, the milk before we use it... we chew salt to see how we like it in our teeth, on our tongues, and to know its flavor, its salinity."</p>
            <p>For the chef, tasting the ingredients tells them whether they are making progress toward their desired end goal. It provides the immediate feedback they need to get the recipe just right.</p>
            <p>Like a chef improving a recipe through trial and error, we often improve our habits through trial and error. If one approach doesn't deliver the desired effect, then we adjust-like a chef tweaking the amount of an ingredient.</p>
            <hr>
            <p class="mb-0">So, what are you waiting for ? Add a tracker now and begin your journey of improving yourself.</p>
        </div>  
        <CreateTrackerModal class="mx-3"/>
    </div>
</template>
<script>
    import CreateTrackerModal from './modals/CreateTrackerModal.vue';
    export default{
        name :'NoTrackerDashboard',
        components:{
            CreateTrackerModal
        }
    }
</script>