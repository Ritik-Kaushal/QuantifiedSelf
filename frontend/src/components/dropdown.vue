<template>
    <div class="container-fluid">
        <div class="row">
          <div class="col-md-12 fw-bold fs-5">
            Choose the tracker and the duration of data
          </div>
        </div>
        <hr class="dropdown-divider" />
        <div class="row">
          <div class="col-md-12">
            <form class="row g-2">
              <div class="col-auto">
                <select
                  class="form-select"
                  aria-label="Default select example"
                  name="tracker_id"
                  v-model="tracker_id"
                >
                <option @click="this.$store.commit('set_update_component');" :id="each.id" v-for="each in $store.getters.get_tracker_list" :key="each.id" :value="each.id" >{{ each.name }}</option>
                </select>
              </div>
              <div class="col-auto">
                <select
                  class="form-select"
                  aria-label="Default select example"
                  name="data_duration_id"
                  v-model="data_duration_id"
                >
                <option @click="this.$store.commit('set_update_component');" :id="each.id" v-for="each in $store.getters.get_duration_list" :key="each.id" :value="each.id" >{{ each.duration }}</option>
                </select>
              </div>
            </form>
          </div>
        </div>
      </div>
</template>

<script>
export default {
name: "DropDown",
mounted(){
  this.tracker_id = this.$store.getters.get_selected_tracker_id;
  this.data_duration_id = this.$store.getters.get_selected_duration_id;

},
data(){
  return{
    tracker_id : -1,
    data_duration_id : 0
  }
},
watch : {
  async tracker_id (newV,oldV){
    // this.$store.commit('set_update_component');
    this.$store.commit('change_selected_tracker_id',newV);
    await this.$store.dispatch("getSelectedTrackerDetails");
  },
  async data_duration_id (newV,oldV){
    // this.$store.commit('set_update_component');
    this.$store.commit('change_selected_duration_id',newV);
    await this.$store.dispatch("update_logs_of_duration");
  }
}

}
</script>
