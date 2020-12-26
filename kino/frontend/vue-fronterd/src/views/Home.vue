<template>
<div class="home" >
  <div v-for="movie in movies" v-bind:key="movie.id">
  <a>{{movie.title}}</a>
  <a> {{movie.middle_rating}}</a>
  <a> {{movie.that_user_rating}}</a>
  </div>
  </div>

</template>


<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
  },
  data(){
    return{
      movies:[]
    }
  },
  async created() {
  var response =await fetch('http://localhost:8000/api/v2/movie/');
  this.movies= await response.json();
  console.log(movies)
  
  }}

</script>
