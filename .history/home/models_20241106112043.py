class HomePage(Page):
    image_slider =StreamField(
        [('image_slider', ImageSliderBlock())], 
        use_json_field=True, 
        blank=True,
        min_num=1,
    ) 