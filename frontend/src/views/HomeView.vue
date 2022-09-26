<template>
  <div id="main-div">
    <div>
      <CarouSel />
    </div>
    <div>
      <router-view />
    </div>
  </div>
</template>

<script>
import CarouSel from "@/components/Carousel.vue";
export default {
  name: "HomeView",
  components: {
    CarouSel,
  },
};
</script>

<style scoped>
/* custom-container class is added to div with id "main-div" when login/register button is clicked from nav bar */
@media screen and (min-width: 990px) {
  .custom-container {
    display: grid;
    grid-template-columns: 3fr 1fr;
  }
}

@media screen and (max-width: 989px) {
  .custom-container {
    display: grid;
    grid-template-rows: 1fr 2fr;
  }
}
@media screen and (max-width: 500px) {
  .custom-container {
    display: grid;
    grid-template-rows: 0.5fr 2.5fr;
  }
}
</style>
