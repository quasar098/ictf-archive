from subprocess import run
from random import choice

fake_flags = [
        "jctf{red_flags_and_fake_flags_form_an_equivalence_class}",
        "jctf{clicking_cant_help_you_now}",
        "jctf{just_cat_the_fish}",
        "jctf{making_fake_flags_is_more_fun_than_making_real_flags}",
        "jctf{This_is_secure_right?}",
        "jctf{powered_by_Flask_tm}",
        "jctf{sourcelesswebaphobia}",
        "jctf{cats_love_fish_fake_flags_and_hash_browns}",
        "jctf{always_eat_potatoes_for_breakfast}",
        "jctf{%s}",
        "jctf{en_passant_is_forced}",
        "jctf{this_will_be_my_fifth_doctorate}",
        "jctf{they_call_me_puzzler_md}",
        "jctf{the_fitness_gram_pacer_test_is_too_long_for_aflag...or_is_it\x07}",
        "jctf{The_FitnessGram™_Pacer_Test_is_a_multistage_aerobic_capacity_test_that_progressively_gets_more_difficult_as_it_continues._The_20-meter_pacer_test_will_begin_in_30_seconds._Line_up_at_the_start._The_running_speed_starts_slowly_but_gets_faster_each_minute_after_you_hear_this_signal._A_single_lap_should_be_completed_each_time_you_hear_this_sound._Remember_to_run_in_a_straight_line,_and_run_as_long_as_possible._The_second_time_you_fail_to_complete_a_lap_before_the_sound,_your_test_is_over._The_test_will_begin_on_the_word_start._On_your_mark,_get_ready,_start.}",
        "jctf{huge_shoutout_to_the_helpers!_they've_been_doing_fantastic_work_in_testing_and_tickets}",
        "jctf{never_gonna_give_you_up}",
        "jctf{never_gonna_let_you_down}",
        "jctf{you_know_the_rules_and_so_do_I}",
        "jctf{https://www.youtube.com/watch?v=dQw4w9WgXcQ%7D",
        "jctf{i_never_use_salt_on_my_potatoes}",
        "jctf{the_equivalence_class_of_fake_flags_and_red_flags_of_course_forms_a_partition_too}",
        "jctf{fake_flags_are_fun}",
        "jctf{you've_heard_of_zyphen_chamber_but_have_you_heard_of_siphon_chamber?_comingsoon(tm)_to_a_daily_challenge_near_you_soon}",
        "jctf{what_even_is_an_equivalence_class}",
        "jctf{?????????????????you_can't_stop_me?????????????????}",
        "jctf{watch_me_put_an_emote_in_a_flag_to_screw_nitrousers:rooPuzzlerDevil:}",
        "jctf{⚑}",
        "jctf{dont_dos_my_server_please_ill_be_sad}",
        "jctf{Also_play_terraria!}",
        "jctf{Also_play_outer_wilds!}",
        "jctf{Also_play_minecraft!}",
        "jctf{one_flag_to_rule_them_all_one_flag_to_find_them}",
        "jctf{one_flag_to_bring_them_all_and_in_the_darkness_bind_them}",
        "jctf{a_hacker_is_just_someone_that_wears_a_hoodie_on_the_internet}",
        "jctf{powered_by_python}",
        "jctf{thx_puzzler_for_the_fake_flags}",

]

cmd = input("$ ")
if "sh" in cmd or len(cmd) > 8 or 'flag' in cmd or 'py' in cmd:
    print(choice(fake_flags))    
    exit()

run(cmd, shell=True)
