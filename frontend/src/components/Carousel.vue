<template>
  <div class="container mt-1">
    <div
      id="carouselExampleFade"
      class="carousel slide carousel-fade"
      data-bs-ride="carousel"
    >
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img
            src="@/assets/homepage/home_carousel_1.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_2.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_3.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_4.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_5.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_6.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_7.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_8.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_9.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_10.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_11.jpg"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleFade"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleFade"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "CarouSel",
};
</script>
