# チーム数を指定した場合のチーム分け
def make_party_num(self, ctx, party_num, remainder_flag='false'):
    team = []
    remainder = []
    
    # メンバーリストを取得
    if self.set_mem(ctx) is False:
        return self.vc_state_err

    # 指定数の確認
    if party_num > self.mem_len or party_num <= 0:
        return '実行できません。チーム分けできる数を指定してください。(チーム数を指定しない場合は、デフォルトで2が指定されます)'

    # メンバーリストをシャッフル
    random.shuffle(self.channel_mem)

    # チーム分けで余るメンバーを取得
    if remainder_flag:
        remainder_num = self.mem_len % party_num
        if remainder_num != 0: 
            for r in range(remainder_num):
                remainder.append(self.channel_mem.pop())
            team.append("=====余り=====")
            team.extend(remainder)

    # チーム分け
    for i in range(party_num): 
        team.append("=====チーム"+str(i+1)+"=====")
        team.extend(self.channel_mem[i:self.mem_len:party_num])

    return ('\n'.join(team))
