<template>
<section class="main-container" >

      <h1 id="tvShows">Категории:</h1>
      <div class="box category">
        <a v-for="category in categories" v-bind:key="category.id" ><img :src="category.poster" alt="" ></a>
      
      </div>
</section>

</template>

<script>
export default {
  name: 'Categories',
  component:{},

    data(){
      return{
        categories:[],
      }
    },
      created() {

        this.loadCategories()
      },
    methods: {
      async loadCategories(){
        this.categories = await fetch(
          `http://127.0.0.1:8000/api/v2/categories/`
        ).then(response=>response.json())
      },
  
      //goTo(url){
        //this.$router.push({name:"OneMovie", params: {url:url} })
      //}
    },
    }

</script>