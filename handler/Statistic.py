from flask import jsonify


class StatisticHandler:
    def DailyResourcesInNeed(self):
        return jsonify(Error="'DailyResourcesInNeed' FAILED. Cannot connect to Database"), 404

    def DailyResourcesAvailable(self):
        return jsonify(Error="'DailyResourcesAvailable' FAILED. Cannot connect to Database"), 404

    def DailyMatching(self):
        return jsonify(Error="'DailyMatching' FAILED. Cannot connect to Database"), 404

    def WeeklyResourcesInNeed(self):
        return jsonify(Error="'WeeklyResourcesInNeed' FAILED. Cannot connect to Database"), 404

    def WeeklyResourcesAvailable(self):
        return jsonify(Error="'WeeklyResourcesAvailable' FAILED. Cannot connect to Database"), 404

    def WeeklyMatching(self):
        return jsonify(Error="'WeeklyMatching' FAILED. Cannot connect to Database"), 404

        def regionResourcesInNeed(self):
            return jsonify(Error="'regionResourcesInNeed' FAILED. Cannot connect to Database"), 404

    def regionResourcesAvailable(self):
        return jsonify(Error="'regionResourcesAvailable' FAILED. Cannot connect to Database"), 404

    def regionMatching(self):
        return jsonify(Error="'regionMatching' FAILED. Cannot connect to Database"), 404