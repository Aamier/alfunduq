from rest_auth.views import LoginView
from users import models


class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "some message", "status": "success"}
        # user = self.user
        user_details = models.CustomUser.objects.get(email=self.user)
        mydata = {
            'is_profile_updated': user_details.is_profile_updated,
            'id': user_details.id
                  }
        orginal_response.data.update(mydata)
        return orginal_response