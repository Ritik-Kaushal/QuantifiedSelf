<template>
    
</template>

<script>
export default{
    name:"LogOut",
    mounted(){
        this.$store.dispatch('logoutUser');
    }
}
</script>
