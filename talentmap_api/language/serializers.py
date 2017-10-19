from rest_framework import serializers

from talentmap_api.common.serializers import PrefetchedSerializer
from talentmap_api.language.models import Language, Proficiency, Qualification, Waiver


class LanguageSerializer(PrefetchedSerializer):

    class Meta:
        model = Language
        fields = "__all__"


class LanguageProficiencySerializer(PrefetchedSerializer):

    class Meta:
        model = Proficiency
        fields = "__all__"


class WaiverSerializer(PrefetchedSerializer):
    position = serializers.StringRelatedField()
    bidcycle = serializers.StringRelatedField()
    language = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Waiver
        fields = "__all__"
        writable_fields = ("position", "bidcycle", "language", "type")


class WaiverWritableSerializer(PrefetchedSerializer):

    class Meta:
        model = Waiver
        fields = "__all__"
        writable_fields = ("position", "bidcycle", "language", "type")


class LanguageQualificationSerializer(PrefetchedSerializer):

    language = serializers.StringRelatedField()
    reading_proficiency = serializers.StringRelatedField()
    spoken_proficiency = serializers.StringRelatedField()
    representation = serializers.SerializerMethodField()

    def get_representation(self, obj):
        return str(obj)

    class Meta:
        model = Qualification
        fields = "__all__"


class LanguageQualificationWritableSerializer(PrefetchedSerializer):

    class Meta:
        model = Qualification
        fields = "__all__"
        writable_fields = ("language", "reading_proficiency", "spoken_proficiency")
