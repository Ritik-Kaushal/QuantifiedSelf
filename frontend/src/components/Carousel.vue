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
            src="@/assets/homepage/home_carousel_1.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_2.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_3.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_4.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_5.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_6.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_7.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_8.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_9.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_10.png"
            class="d-block"
            :style="{ width: this.$store.getters.get_carousel_width + '%' }"
            alt="..."
          />
        </div>
        <div class="carousel-item">
          <img
            src="@/assets/homepage/home_carousel_11.png"
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
