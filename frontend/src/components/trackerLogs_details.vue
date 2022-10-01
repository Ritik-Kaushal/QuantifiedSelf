<template>
  <div>
    <div class="container-fluid">
      <!-- Divider -->
      <hr class="dropdown-divider" />
      <!-- Divider -->

      <div class="row mt-2">
        <div class="col-md-12 fw-bold fs-5 text-center mt-5">
          Logs of {{ $store.getters.get_selected_tracker.tracker_name }} Tracker
        </div>
      </div>

      <!-- Divider -->
      <hr class="dropdown-divider" />
      <!-- Divider -->

      <div class="row mt-2">
        <table class="table table-stripped table-hover">
          <thead>
            <tr>
              <th scope="col">S.N.</th>
              <th scope="col">Timestamp</th>
              <th scope="col">Value</th>
              <th scope="col">Note</th>
              <th scope="col">Tracker Name</th>
              <th scope="col">Tracker Type</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(eachLog, index) in $store.getters.get_reqd_duration_logs"
              :key="eachLog.id"
            >
              <th scope="row">{{ index + 1 }}</th>
              <td>{{ eachLog.time_stamp }}</td>
              <td>{{ eachLog.value }}</td>
              <td>{{ eachLog.note }}</td>
              <td>{{ $store.getters.get_selected_tracker.tracker_name }}</td>
              <td>{{ $store.getters.get_selected_tracker.tracker_type }}</td>
              <td>
                <UpdateLogModal
                  :modal_id="'UpdateLogModal' + eachLog.id"
                  :log="eachLog"
                />
                <DeleteLogModal
                  :modal_id="'deleteLogModal' + eachLog.id"
                  :log_id="eachLog.id"
                />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Divider -->
      <hr class="dropdown-divider" />
      <!-- Divider -->
      <div class="pb-2 mb-5">
        <LogValueModal />
      </div>
    </div>
  </div>
</template>

<script>
import DeleteLogModal from "./modals/DeleteLogModal.vue";
import UpdateLogModal from "./modals/UpdateLogModal.vue";
import LogValueModal from "./modals/LogValueModal.vue";
export default {
  name: "TrackerLogs_Details",
  components: {
    DeleteLogModal,
    UpdateLogModal,
    LogValueModal
  },
  methods: {},
};
</script>
