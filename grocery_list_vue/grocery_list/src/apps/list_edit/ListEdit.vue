<template>
    
    <form method="post" class="form">
        <input type="hidden" name="csrfmiddlewaretoken" v-bind:value="csrf_token">
        <p>
            <label for="id_name">Name:</label>
            <input type="text" name="name" v-model="glist_name" maxlength="100" required="" id="id_name">
        </p>

        <p>
            <label for="id_groceries">Groceries:</label>
            <select hidden name="groceries" required="" id="groceries" multiple="">
                <option v-for="grocery in grocery_list" :value="grocery.name" selected=""></option>
            </select>

            <multiselect v-model="grocery_list" :options="grocery_list_source" :multiple="true" :close-on-select="false"
                :clear-on-select="false" :preserve-search="true" placeholder="Choose the groceries" label="name"
                track-by="name" :preselect-first="true"
                style="display:inline-block;width: 300px;padding-bottom:10px;padding-left:10px">
                <template slot="selection" slot-scope="{ values, search, isOpen }"><span class="multiselect__single"
                        v-if="values.length" v-show="!isOpen">{{ values.length }} options selected</span></template>
            </multiselect>

        </p>

        <button type="submit" class="btn btn-primary">
            Submit
        </button>
    </form>



</template>


<script>
import '@vuepic/vue-datepicker/dist/main.css'
import Multiselect from 'vue-multiselect'


export default {
    name: 'App',
    components: {
        Multiselect
    },
    data: function () {
        return {
            csrf_token: ext_csrf_token,
            form: ext_form,
            glist_dico: ext_glist_dict,
            grocery_list_source: ext_grocery_list,
            grocery_list:ext_glist_dict.groceries,
            glist_name: ext_glist_dict.name

        }
    },

    methods: {

    },
    computed: {
    },
    mounted() {
        this.csrf_token = ext_csrf_token,
        this.form = ext_form,
        this.glist_dico = ext_glist_dict,
        this.grocery_list_source = ext_grocery_list,
        this.grocery_list = ext_glist_dict.groceries

    }
}



</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>
