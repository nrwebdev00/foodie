from multiprocessing import context
from django.shortcuts import render, redirect
from .models import (
                    Recipe,
                    Recipe_Comments,
                    Recipe_Directions,
                    Recipe_Images,
                    Recipe_Ingredients,
                    Recipe_Video
                )
from .forms import (RecipeCommentForm,
                    RecipeDirectionsForm,
                    RecipeForm,
                    RecipeImageForm,
                    RecipeIngredientsForm,
                    RecipeVideoForm,
                )


def recipes(request):
    recipes = Recipe.objects.all()
    # courses_tags = Recipe.objects.filter(courses_tag__name="Lunch")

    print(request.user.profile)

    context = {'recipes': recipes, }

    return render(request, 'recipe/recipe.html', context)


# Create Recipe
def create_recipe(request):
    profile = request.user.profile
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'recipe/recipe_form.html', context )

# Create Recipe-Comment
def create_recipe_comment(request, id):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=id)
    form = RecipeCommentForm()

    if request.method == 'POST':
        form = RecipeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = profile
            comment.recipe = recipe
            comment.save()
            return redirect('home')

    context = {'form': form }

    return render(request, 'recipe/recipe_form.html', context)

# Create Recipe-Directions
def create_recipe_directions(request, id):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=id)
    form = RecipeDirectionsForm()

    if request.method == 'POST':
        form =RecipeDirectionsForm(request.POST)
        if form.is_valid():
            direction = form.save(commit=False)
            direction.owner = profile
            direction.recipe = recipe
            direction.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'recipe/recipe_form.html', context)

# Create Recipe-Ingredients
def create_recipe_ingredient(request, id):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=id)
    form = RecipeIngredientsForm()

    if request.method == 'POST':
        form = RecipeIngredientsForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.owner = profile
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'recipe/recipe_form.html', context)

# Create Recipe-Video
def create_recipe_video(request, id):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=id)
    form = RecipeVideoForm()

    if request.method == 'POST':
        form = RecipeVideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.owner = profile
            video.recipe = recipe
            video.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'recipe/recipe_form.html', context)

# Create Recipe-Image
def create_recipe_image(request, id):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=id)
    form = RecipeImageForm()

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = profile
            image.recipe = recipe
            image.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'recipe/recipe_form.html', context)


# Update Recipe
def update_recipe(request, id):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=id)
    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe_updated = form.save(commit=False)
            recipe_updated.owner = profile
            recipe_updated.recipe = recipe
            recipe_updated.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'recipe/recipe_form.html', context )

# Update Recipe-Comment
def update_recipe_comment(request, id):
    profile = request.user.profile
    comment = Recipe_Comments.objects.get(id=id)
    recipe = comment.recipe
    form = RecipeCommentForm(instance=comment)

    if request.method == 'POST':
        form = RecipeCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment_updated = form.save(commit=False)
            comment_updated.owner = profile
            comment_updated.recipe = recipe
            comment_updated.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'recipe/recipe_form.html', context)

# Update Recipe-Directions
def update_recipe_directions(request, id):
    profile = request.user.profile
    direction = Recipe_Directions.objects.get(id=id)
    recipe = direction.recipe
    form = RecipeDirectionsForm(instance=direction)

    if request.method == 'POST':
        form = RecipeDirectionsForm(request.POST, instance=direction)
        if form.is_valid():
            direction_updated = form.save(commit=False)
            direction_updated.owner = profile
            direction_updated.recipe = recipe
            direction_updated.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'recipe/recipe_form.html', context)

# Update Recipe-Ingredients
def update_recipe_ingredients(request, id):
    profile = request.user.profile
    ingredient = Recipe_Ingredients.objects.get(id=id)
    recipe = ingredient.recipe
    form = RecipeIngredientsForm(instance=ingredient)

    if request.method == 'POST':
        form = RecipeIngredientsForm(request.POST, instance=ingredient)
        if form.is_valid():
            ingredient_updated = form.save(commit=False)
            ingredient_updated.owner = profile
            ingredient_updated.recipe = recipe
            ingredient_updated.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'recipe/recipe_form.html', context)

# Update Recipe-Video
def update_recipe_video(request, id):
    profile = request.user.profile
    video = Recipe_Video.objects.get(id=id)
    recipe = video.recipe
    form = RecipeVideoForm(instance=video)

    if request.method == 'POST':
        form = RecipeVideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            video_updated = form.save(commit=False)
            video_updated.owner = profile
            video_updated.recipe = recipe
            video_updated.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'recipe/recipe_form.html', context)

# Update Recipe-Image
def update_recipe_image(request, id):
    profile = request.user.profile
    image = Recipe_Images.objects.get(id=id)
    recipe = image.recipe
    form = RecipeImageForm(instance=image)

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES, context)
        if form.is_valid():
            image_updated = form.save(commit=False)
            image_updated.owner = profile
            image_updated.recipe = recipe
            image_updated.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'recipe/recipe_form.html', context)

# Delete Recipe
def delete_recipe(request, id):
    profile = request.user.profile
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')

    context = {'object': recipe}

    return render(request, 'recipe/recipe_delete_template.html', context)

# Delete Recipe-Comment
def delete_recipe_comment(request, id):
    comment = Recipe_Comments.objects.get(id=id)

    if request.method == 'POST':
        comment.delete()
        return redirect('home')

    context = { 'object': comment}

    return render(request, 'recipe/recipe_delete_template.html', context)

# Delete Recipe-Directions
def delete_recipe_direction(request, id):
    direction = Recipe_Directions.objects.get(id=id)

    if request.method == 'POST':
        direction.delete()
        return redirect('home')

    context = {'object': direction}

    return render(request, 'recipes/recipe_delete_template.html', context)

# Delete Recipe-Ingredients
def delete_recipe_ingredients(request, id):
    ingredient = Recipe_Ingredients.objects.get(id=id)

    if request.method == 'POST':
        ingredient.delete()
        return redirect('home')

    context = {'object': ingredient}

    return render(request, 'recipe/recipe_delete_template.html', context)

# Delete Recipe-Video
def delete_recipe_video(request, id):
    video = Recipe_Video.objects.get(id=id)

    if request.method == 'POST':
        video.delete()
        return redirect('home')

    context = {'object': video}

    return render(request, 'recipe/recipe_delete_template.html', context)

# Delete Recipe-Image
def delete_recipe_image(request, id):
    image = Recipe_Images.objects.get(id=id)

    if request.method == 'POST':
        image.delete()
        return redirect('home')

    context = {'object': image}

    return render(request, 'recipe/recipe_delete_template.html', context)