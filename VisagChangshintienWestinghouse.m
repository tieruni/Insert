//
//  TTStrRE.m
//  urlencodeSet
//
//  Created by blaceman on 2020/7/10.
//  Copyright © 2020 blaceman. All rights reserved.
//

#import "VisagChangshintienWestinghouse.h"

@implementation VisagChangshintienWestinghouse
+ (NSString *)PoekzVojvodinaTallahassee:(NSString *)urlString{
    NSString *str2 = [urlString stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];//url编码解码
//    NSString *str2 = [urlString stringByRemovingPercentEncoding];//url编码解码
    
    NSArray *nameAtt = [str2 componentsSeparatedByString:@"^*^"];
    
    NSData *dictData = [NSKeyedArchiver archivedDataWithRootObject:nameAtt]; //归档
    NSArray *subDict = [NSKeyedUnarchiver unarchiveObjectWithData:dictData]; //还原
    NSMutableArray *muArr = [NSMutableArray arrayWithArray:subDict];
    muArr[0] = [NSString stringWithFormat:@"%c",((NSString *)muArr[0]).intValue];
    NSString *string = [muArr componentsJoinedByString:@""];

    string = [string stringByReplacingOccurrencesOfString:@"trp:o*yq" withString:@""];

    NSLog(@"还原后的:%@",string);

    return string;
}


+ (NSData *)PoekzPedicellinidaeZinjanthropine:(NSData *)encodeData{
    NSString *urlString = [[NSString alloc]initWithData:encodeData encoding:NSUTF8StringEncoding];

    
    
    NSString *str2 = [urlString stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];//url编码解码
//    NSString *str2 = [urlString stringByRemovingPercentEncoding];//url编码解码
    
    NSArray *nameAtt = [str2 componentsSeparatedByString:@"^*^"];
    
    NSData *dictData = [NSKeyedArchiver archivedDataWithRootObject:nameAtt]; //归档
    NSArray *subDict = [NSKeyedUnarchiver unarchiveObjectWithData:dictData]; //还原
    NSMutableArray *muArr = [NSMutableArray arrayWithArray:subDict];
    muArr[0] = [NSString stringWithFormat:@"%c",((NSString *)muArr[0]).intValue];
    NSString *string = [muArr componentsJoinedByString:@""];

    string = [string stringByReplacingOccurrencesOfString:@"trp:o*yq" withString:@""];

//    NSLog(@"还原后的:%@",string);

    return [string dataUsingEncoding:NSUTF8StringEncoding];
}

@end
