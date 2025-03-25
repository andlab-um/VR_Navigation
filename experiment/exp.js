function shuffle_twolist(list1, list2) {
    // Create shuffled index based on length of list1
    const shuffled_indices = [...Array(list1.length).keys()].sort(() => Math.random() - 0.5);
  
    // Create shuffled lists using the generated indices
    const shuffled_list1 = shuffled_indices.map((i) => list1[i]);
    const shuffled_list2 = shuffled_indices.map((i) => list2[i]);
  
    return [shuffled_list1, shuffled_list2];
  }

const scenes = ["label1", "label2", "label3", "label4", "label5", "label6", "label7", "label8", "label9", "label10", "label11", "label12", "label13", "label14"];
const scene_value = ["flower", "bin", "sofa", "plant", "mailbox", "wash", "CaseAvatar1", "CaseAvatar2", "CaseAvatar3", "CaseAvatar4", "CaseAvatar5", "CaseAvatar6", "CaseAvatar7", "CaseAvatar8"];

// Shuffle the scenes and values
const [new_scenes, new_scene_value] = shuffle_twolist(scenes, scene_value);

console.log(new_scenes);
console.log(new_scene_value);