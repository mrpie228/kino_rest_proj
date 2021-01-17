<template>
<div>
<section class="main-container" >
  <div class="profile">
  <div class="location" id="one_film">

          <h1 id="home">{{profile_information.user.username}}</h1>
          <h3>Watch Later:</h3>
          <h4 v-for="later in profile_information.watch_later" v-bind:key="later.id" >{{later.title}}</h4>
          <h3>What Liked:</h3>
          <h4 v-for="what_liked in profile_information.liked" v-bind:key="what_liked.id" >{{what_liked.title}}</h4>

  </div>
  </div>
</section>
</div>
</template>


<script>
export default {
  name: 'Profile',
  props:['id'],
 
  data(){
    return{
      profile_information:{}, 

      
    }
  },
  created() {
      this.loadProfile()
    },
  methods: {
    async loadProfile(){

      this.profile_information = await fetch(
        `http://127.0.0.1:8000/profiles/profile/${this.id}`
      ).then(response=>response.json()).then(console.log(this.profile_information))
    },
  }
}
</script>
