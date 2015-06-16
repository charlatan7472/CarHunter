import DesiredOptions
# site_name = "http://www.autotrader.com"
"""base_string = '/cars-for-sale/searchresults.xhtml?' \
                '&zip=32202' \
                '&extColorsSimple=BLACK%2CBLUE&exteriorColorSimple1=BLACK&exteriorColorSimple2=BLUE' \
                '&searchRadius=0' \
                '&doorCodes=4' \
                '&featureCodes=1078%2C1132' \
                '&makeCode1=RAM' \
                '&trim1=RM1500%7CSport' \
                '&mmt=%5BRAM%5BRM1500%5BRM1500%7CSport%5D%5D%5B%5D%5D' \
                '&maxMileage=45000' \
                '&vehicleStyleCodes=TRUCKS' \
                '&minPrice=0' \
                '&maxPrice=35000' \
                '&listingTypes=used%2Ccertified' \
                '&startYear=2012' \
                '&endYear=2015' \
                '&sellerTypes=d' \
                '&mod_bookmark_id=102332494&lastExec=1433529371000'
"""

autotrader_feature_lookup = {'LeatherSeats': '1078', 'Sunroof': '1132'}
# for debugging




def set_search_string(site, options):
    """
    creates and sets a string that provides a search url
    :rtype : string
    """
    search_string = ""
    if site == "www.autotrader.com":
        search_string += '/cars-for-sale/searchresults.xhtml?'
        assert isinstance(options, DesiredOptions.DesiredOptions)

        # setting up auto trader zip code parameter
        if options.zipcode() is not None:
            search_string = search_string + '&zip=' + options.zipcode()
        else:
            search_string += '&zip=32250'

        # handling auto trader exterior color parameters
        color_list = options.external_colors()
        if color_list.count > 0:
            # Need to validate to make sure this is a usable color
            ext_colors_string = '&extColorsSimple='
            ext_color_string = ''
            for index, color in enumerate(color_list):
                if color == color_list[-1]:
                    ext_colors_string += color.upper()
                else:
                    ext_colors_string += color.upper() + '%2C'
                ext_color_string += '&exteriorColorSimple' + str(index + 1) + '=' + color.upper()
            search_string += ext_colors_string + ext_color_string

        # setting up Autotrader search radius options
        if options.search_radius() is not None:
            search_string += '&searchRadius=' + options.search_radius()
        else:
            search_string += '&searchRadius=0'

        # setting up Autotrader door code options
        if options.number_of_doors() is not None:
            search_string += '&doorCodes=' + options.number_of_doors()

        # setting up Autotrader feature code options
        feature_list = options.features()
        if feature_list.count > 0:
            # Need to validate to make sure this is a usable color
            features_string = ''
            for index, feature in enumerate(feature_list):
                if feature == feature_list[-1]:
                    features_string += autotrader_feature_lookup[feature]
                else:
                    features_string += autotrader_feature_lookup[feature] + '%2C'
            search_string += features_string

        '&makeCode1=RAM' \
                '&trim1=RM1500%7CSport' \
                '&mmt=%5BRAM%5BRM1500%5BRM1500%7CSport%5D%5D%5B%5D%5D' \
        #autotrader make code
        

    print search_string
