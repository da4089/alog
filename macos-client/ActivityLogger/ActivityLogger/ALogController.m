//
//  ALogController.m
//  ActivityLogger
//
//  Created by David Arnold on 29/03/14.
//  Copyright (c) 2014 David Arnold. All rights reserved.
//

#import "ALogController.h"

@implementation ALogController
- (id)init
{
    self = [super init];
    if (self) {
        // Initialise here
    }
    
    NSLog(@"Controller got init.\n");
    
    // Try to start window as modal
    //[NSApp runModelForWindow];
    return self;
}


- (void)dealloc
{
    // this is flagged as an issue with ARC: [super dealloc];
}


- (void)awakeFromNib
{
    NSLog(@"Controller got awakeFromNib.\n");
}


- (IBAction)cancel:(id) sender
{
    NSLog(@"Controller got cancel.\n");
}


- (IBAction)ok:(id)sender
{
    NSLog(@"Controller got ok.\n");
    
    // Hide window
    //[taskWindow orderOut:self];
    //char buf[200];
    //[[comboBox stringValue] getCString:buf maxLength:200 encoding:NSASCIIStringEncoding];
    
    NSLog(@"Combo text: %@\n", [comboBox stringValue]);
}

@end
