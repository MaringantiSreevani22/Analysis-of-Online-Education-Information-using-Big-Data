
import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        "student_id": ["s1", "s2", "s1", "s3", "s2", "s1", "s3", "s4"],
        "course_id": ["course_101", "course_101", "course_102", "course_101",
                      "course_103", "course_101", "course_102", "course_104"],
        "activity_type": ["video_watch", "quiz_attempt", "video_watch", "video_watch",
                          "forum_post", "quiz_attempt", "video_watch", "video_watch"],
        "timestamp": [
            "2025-05-18 10:00:00",
            "2025-05-18 11:15:00",
            "2025-05-18 12:00:00",
            "2025-05-18 10:05:00",
            "2025-05-18 14:00:00",
            "2025-05-18 10:30:00",
            "2025-05-18 13:00:00",
            "2025-05-18 15:00:00",
        ],
    }

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    print("\n===== RAW DATA =====")
    print(df)

    active_users_count = df["student_id"].nunique()
    print(f"\nTotal distinct active users: {active_users_count}")

    popular_courses = (
        df["course_id"]
        .value_counts()
        .rename_axis('course_id')
        .reset_index(name='activity_count')
    )

    print("\n===== MOST POPULAR COURSES =====")
    print(popular_courses)

    df["hour"] = df["timestamp"].dt.hour

    activity_by_hour = (
        df.groupby("hour")
        .size()
        .reset_index(name='activity_count')
        .sort_values(by="hour")
    )

    print("\n===== ACTIVITY BY HOUR =====")
    print(activity_by_hour)

    plt.figure(figsize=(8, 4))
    plt.bar(popular_courses['course_id'], popular_courses['activity_count'])
    plt.title('Most Popular Courses')
    plt.xlabel('Course ID')
    plt.ylabel('Activity Count')
    plt.tight_layout()
    import os
    os.makedirs("visualizations", exist_ok=True)
    plt.savefig("visualizations/popular_courses.png")

    plt.figure(figsize=(8, 4))
    plt.bar(activity_by_hour['hour'], activity_by_hour['activity_count'])
    plt.title('Activity by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Activity Count')
    plt.tight_layout()
    plt.savefig("visualizations/activity_by_hour.png")

    print("\nCharts saved in visualizations folder.")

if __name__ == "__main__":
    main()
